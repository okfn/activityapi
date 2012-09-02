from github import Github
from dash.backend import Session
from dash.backend.model import Repo, SnapshotOfRepo, Person, EventGithub
from datetime import datetime,timedelta

def scrape_repos(verbose=False):
    if verbose: print 'Connecting to GitHub...'
    gh = Github()
    if verbose: print 'Fetching profile for "okfn"...'
    okfn = gh.get_organization('okfn')
    if verbose: print 'Scraping repository list (slow)...'
    out = { x.full_name : x for x in okfn.get_repos() }
    if verbose: print 'Got %d repos.' % len(out)
    assert len(out) > 0, 'Wont proceed without receiving some repos from server.'
    return out

def save_repos(gh_repos, verbose=False):
    """Update the 'repo' table"""
    # Add and update
    for k,v in gh_repos.items():
        # v is a dict of a 'repo' (from our ORM) and a 'gh_repo' (from the library)
        repo = Session.query(Repo).filter(Repo.full_name==k).first()
        if repo:
            repo.update(v)
        else:
            if verbose: print 'Adding new repo %s' % v.full_name
            repo = Repo(v)
            Session.add(repo)
    # Delete
    for repo in Session.query(Repo):
        if not repo.full_name in gh_repos:
            if verbose: print 'Deleting repo %s' % repo.full_name
            Session.delete(repo)
    # Commit now to ensure repo.id is auto-assigned
    Session.commit()

def snapshot_repos(gh_repos, verbose=False):
    """Create SnapshotOfRepo objects in the database for 
       every day since the last time this was run."""
    day = timedelta(days=1)
    today = datetime.now().date()
    until = today - day
    for r in Session.query(Repo):
        if verbose: print 'Processing snapshots for %s...' % r.full_name
        latest = Session.query(SnapshotOfRepo)\
                .filter(SnapshotOfRepo.repo_id==r.id)\
                .order_by(SnapshotOfRepo.timestamp.desc())\
                .first()
        # By default, gather 30 days of snapshots
        since = until - timedelta(days=30)
        if latest:
            if latest.timestamp>=until:
                if verbose: print ' -> most recent snapshots have already been processed.'
                continue
            since = latest.timestamp + day
        # Snapshot date for the last day (or more)
        gh_repo = gh_repos[ r.full_name ]
        while since <= until:
            snapshot = SnapshotOfRepo( since, r.id, gh_repo.open_issues, gh_repo.size, gh_repo.watchers, gh_repo.forks )
            if verbose: print '  -> ',snapshot.json()
            Session.add(snapshot)
            since += timedelta(days=1)
        Session.commit()


# Activity scrapers

def scrape_github_activity(verbose=False):
    q = Session.query(Person).filter(Person.github!=None)
    gh = Github()
    for x in q:
        if verbose: print 'Scraping events for %s (%s)...' % (x.display_name,x.login)
        gh_user = gh.get_user(x.github)
        _scrape_user_events( x.id, gh_user, verbose )
    Session.commit()
  
def _scrape_user_events( user_id, gh_user, verbose=False ):
    max = 30
    _latest = Session.query(EventGithub).filter(EventGithub.user_id==user_id).order_by(EventGithub.id.desc()).first()
    latest = _latest.id if _latest else 0
    if verbose: print '  latest=%d' % latest
    for x in gh_user.get_events():
        if max <= 0:
            if verbose: print '  scraped 30 events.'
            break
        if int(x.id) <= latest:
            if verbose: print '  scraped %d events. (no further events available)'%(30-max)
            break
        if verbose: print '  > type=%s  id=%s' % (x.type,x.id)
        Session.add( EventGithub(user_id, x) )
        max -= 1

