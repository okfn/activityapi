import tweepy
import os

def twitter_list_name(username):
      l = username[0] 
      if l<'0': raise ValueError(l)
      if l<='_': return 'okfn_0_9'
      if l<='d': return 'okfn_a_d'
      if l<='j': return 'okfn_e_j'
      if l<='r': return 'okfn_k_r'
      if l<='z': return 'okfn_s_z'
      raise ValueError(l)

def twitter_update_lists(names,lists):
  for x in names:
    try:
      lists[twitter_list_name(x)].add_member(x)
      print 'done:',x
    except tweepy.error.TweepError:
      print 'failed to add',x

def api():
    consumer_key = 'G9JTBcBgRWFGTPnjVsL9g'
    access_token = '726428108-cIXizVVYrBGRhTnbxeXAHgA05VpkvtIGAqGEqT9a'
    consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
    access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
    assert consumer_secret and access_token_secret, 'Set environment variables: "TWITTER_CONSUMER_SECRET" and "TWITTER_ACCESS_TOKEN_SECRET" to access the API. (https://dev.twitter.com/apps/2927379/oauth)'
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    return tweepy.API(auth)

def names_cached(): 
    return ['rufuspollock', 'ianibbo', 'jwyg', 'timjph', 'ddie', 'openreflections',
            'nickstenning', 'stekosteko', 'thejimmyg', 'brianglanz', 'stiivi', 'frabcus',
            'misologie', 'jasonkitcat', 'acka47', 'napo', 'cottagelabs', 'todrobbins',
            'julianlstar', 'zoltanvarju', 'carnetsdm', 'band', 'kfasimpaur', 'tommoritz',
            'iainemsley', 'mickmorrison', 'fsdfsd', 'pallih', 'nicoleesmith', 'davidpidsley',
            'jaumetet', 'mikechelen', 'jindrichmynarz', 'apoikola', 'korel_cz', 'acracia',
            'wwitzel3', 'mcdawg', 'stefanwehrmeyer', 'josefjer', 'sinoficina', 'yedpodtrzitko',
            'timclicks', 'laux_and_law', 'saibhaskar', 'sebbacon', 'regardscitoyens', 'fdsfdsf',
            'timdavies', 'einsteinu', 'hockendougal', 'lucyfedia', 'fccoelho', 'ibegtin',
            'rjw', 'bartrosseau', 'joanmulvihill', 'dorukbayer', 'svenmw', 'bniemannsr',
            'fscrollini', 'ddraper', 'lorry', 'everton137', 'metaflask', 'h2cm',
            'bmwelby', 'jimregan', 'tomdemp', 'johannesmarat', 'b2bspecialist', 'mapcuk',
            'jmmarquez', 'ckreutz', 'fasfda', 'aabella', 'whwi', 'martinedelbroek',
            'fsd', 'ef', 'dutchspring', 'adfg', 'emersonvinicius', 'hochstenbach',
            'handelaar', 'china', 'nikhiljs', 'marcomb', 'gutam2000', 'fdfdf',
            'daiey', 'dfxhdf', 'vaccaricarlo', 'openshakespeare', 'fredpalma', 'dggfhfhgh',
            'bejj', 'gertudermcnair1234', 'wetre', 'kat_braybrooke', 'apple', 'timspeak',
            'dav_stott', 'lisiqintongzhou', 'melanieddr', 'scinoptica', 'tuliomac', 'replicahermes',
            'marianeicu', 'mailo73', 'technogiclee', 'lswn2000', 'villavec', 'abelcainefiji',
            'anotherjohng', 'slash', 'marktfahey', 'donnapuff', 'sdff', 'amercader',
            'richlitt', 'cconlyone', 'kat_braybrooke', 'jm_casanueva', 're_linguistics', 'casaesdiego',
            'gulimujyujyu', 'stefankasberger', 'radosvetav', 'rmounce', 'dudhin', 'scheeinfo',
            'leisa', 'graci_selaimen', 'evomri', 'digisus', 'darkgreener', 'tranlib',
            'driven_by_data', 'yaso', 'justinarenstein', 'srini74', 'el_miguelote', 'serinformaticos',
            'jwvaneck', 'dirdigeng', 'netnomade', 'infosidi', 'titetodesco', 'fontanon',
            'gestionpublicav', 'bratsas', 'jeanfred', 'buxninja', 'gillhamilton', 'cognidox',
            'kifcaliph', 'klausz', 'elizita', 'lilia_bcn', 'howa01', 'pizzarebbe',
            'zbeauvais', 'leeworden', 'nilleren', 'aidtransparency', 'gvanlandeghem', 'johnlsheridan',
            'jesgar', 'abhik1368', 'mhanwell', 'harry_wood', 'shevski', 'aothmane31416',
            'marks4maryland', 'g_kn', 'googleclone', 'kommrad', 'svnee', 'dinugherman',
            'robertharm', 'harpandsoul1', 'sdsa', 'rickmurphy', 'coreation', 'kashyapa',
            'wmijnhardt', 'joeygraham', 'xj123456', 'dd', 'marrys', 'jundian123',
            'data_blog', 'china', 'koolhead17', 'indicati', 't', 'sakdfjsak',
            'haha', 'jacques_bus', 'marcianotributa', 'doro', 'fsdf', 'dsfaads',
            'xvzx', 'hjy512339041', 'shownde', 'oneselfyou', 'payo', 'ninadawes',
            'owentsmith', 'dsfaads', 'wanna', 'good', 'mila_frerichs', 'adamhuffman',
            'gracefool', 'fh', 'sdfsdfdsf', 'thillzilla', 'giaccai', 'fgf',
            'pietercolpaert', 'christian', 'piezanowski', 'xiaoya', 'phy', 'carl_grant',
            'hiperterminal', 'tvol', 'schun', 'mediendidaktik', 'thatguylam', 's_kilo',
            'bookpatrol', 'belladead', 'sasa', 'klortho', 'cboettig', 'jamesemmott',
            'jtyu', 'aindhy', 'doctorohm', '404040', 'cbmttgm', 'lucienlegrey',
            'mrpcca', 'mymoneylink', 'senatorjeong', 'stevieflow', 'brunomertins', 'afdsasdf',
            'zhougoosey', 'dantexier', 'tiacarr', 'alenapopova', 'fasda', 'dotunbabayemi',
            'stanneberger', 'fhfhtrj', '68melstevens', 'sdfsdgfdg', 'sdfsdfsgdfg', 'dfgfdf',
            'zephod', 'carolinebeavon', 'owenmundy', 'caef', 'anjesh', 'markherringer',
            'siva_epari', 'gonzaloiglesias', 'tropical', 'svigneau', 'dawmusicmanumit', 'hushin',
            'inso_callcenter', 'semwebcompany', 'teofobo', 'harkanwalhothi', 'jdsfsd', 'kliehm',
            'kattanasio', 'david_mitton', 'raphaelohnsorg', 'kapriforce', 'fd', 'mymoneylink',
            'wahdjh', 'xmacex', 'kmarysmith', 'no', 'fgu', 'zoltanctoth',
            'scriptshifter', 'tujk', 'alextarologo', 'javonliu', 'eirrangeek', 'jaybhalla',
            'alkags', '222ie', 'dsaa', 'viejosaulo', 'ovbhadofivh', 'vndimitrova',
            'davanac', 'kevixaqtmo', 'lauriej', 'bernierussell', 'noel_mas', 'carnops',
            'laatpay', 'aa', 'dry', 'cybernostra', 'hngh', 'dsadsa',
            'sdsadd', 'bhojarajugunjal', 'dfgsdf', 'dumpita', 'northface888', 'romain_kidd',
            'walterebert', 'epoz', 'ptreadwell', 'north', 'ugg', 'timrich',
            'hanachronism', 'alihurriyetoglu', 'chatanimesh', 'newmanlk', 'karengabriels', 'jerome67',
            'sdfsdfsgdfg', 'alexander07', 'dgraziotin', 'dfdf', 'miskaknapek', 'danielbishton',
            'sdfas', 'howard55', 'lievenjanssen', 'zhougoosex', 'josepfigols', 'kousil',
            'cccccc', 'ejanderton', 'dfd', 'htj', 'ben_edictus', 'tarmotoikkanen',
            'dfd', 'naomilillie', 'customusb', 'jasemckenzie', 'trevor60', 'driveway',
            'fdasfsd', 'anaisparenteau', 'bhangbhangduc', 'warenyciam', 'ehujtresju', 'shallumcooper',
            'sdsf', 'raytch', 'peter02', 'northfaceac', '22', 'jonas_agx',
            'mvhst', 'pixeline', 'spilumberto', 'jpekel', 'relet', 'descubrimomento',
            'chawlaanirudh', 'crgonzalez', 'gasdf', 'cheap', 'rw3', 'fi_flossmanuals',
            'fasdf', 'gwebmaster2', 'skokoyo', 'greboun', 'ghfhf', '34234223',
            'nethunt', 'jack_carlson', 'fotiszygoulis', 'philippecyr', 'fdsfsdaf', 'nicoleebeale',
            'bogomep', 'morningside', 'zephod', 'wedding', 'clifffowler2', 'mbrinkerink',
            'alvarograves', 'mzeinstra', 'mintcanary', 'necro144', 'msongari', 'monostich',
            'marja_p', 'riparchivist', 'lawrence', 'jspatton53', 'jburnmurdoch', 'thejbf',
            'revjonb', 'weddingdressesy', 'wodkaundkaviar', 'dmtundu', 'lethanow', 'johnnyryan',
            'darthger', 'jumpbranding', 'misael', 'wedding', 'jamescarnell007', 'paolaricaurte',
            'yc667dwv', 'amirhhz', 'leclezim', 'kompani101', 'eskorthatti', 'geogrr',
            'larjohns', 'lizzabobster01', 'mdh102559', 'jimkont', 'pathadley', 'canwecanwe',
            'mimiss', 'lasersaur', 'jquesadava', 'villum', 'parapontisj', 'findthesky',
            'new_edu', 'niguanigua', 'duncan_ids', 'lambo', 'jaylee0221', 'yc668dwv',
            'dndfsesterp', 'gaelvergier', 'distillr', 'aidanmacguill', 'nigini', 'b_b_b_a_r_t',
            'fefedimoraes', 'jonmbithi', 'paraschos', 'lkeriacom', 'djq', 'stefandietze',
            'bioflukes', 'sauropodmike', 'jackeywall', 'ghfhf', 'apesoapeso', 'janpawlowski',
            'khotin', 'stefania_druga', 'balaitous', 'lottebelice', 'ddjournalism', 'acclar',
            'ffffff', 'lupicinio', 'daveparkes', 'tonykamlesh', 'ayayodhia', 'protohedgehog',
            'dcarvetta007', 'complinayde01', 'dicepb', 'js_bird', 'jurate', 'nishmadoshi',
            'matlocksarah', 'jsimot', 'leathericon', 'zz', 'paulocwb2003', 'olympiaze',
            'lgatt0', 'sheldon_kelly', 'langtry_girl', 'cadat', 'flandqvist', 'marcio_de_assis',
            'ahnchangwon', 'asdf', 'hbunke', 'madlabnl', 'cmarctaylor', 'imonteroperez',
            'andrewjskatz', 'openp2pdesign', 'andreasamsler', 'oageek', 'benrepeatben', 'trox',
            'amberplatform', 'canada', 'openplaques', 'gdfgd', 'crowlineuk', 'lintinglin',
            'egonwillighagen', 'sverbic', 'geraki', 'thedanawinner', 'mrtinoff', 'paullop',
            'fdfgdfg', 'rossjones', 'otisyves', 'lhtorres', 'patriciomolina', 'dfd',
            'true', 'deniskrivosheev', 'claireystew', 'circecon', 'ezkl', 'fremiti',
            'slmnhq', '_giravolta_', 'jiwanowa', 'caccioly', 'socscidirectory', 'ronyoung',
            'salgado', 'insysion', 'okezie', 'sieurope_sie', 'lorenzosol', 'omnireso',
            'attemptedxe', 'watzzupsport', 'rommelnc', 'guzmanadrian', 'poggs', 'fsaviron',
            'digitalrn_sil', 'pacoreyes', 'imsweetie', 'elenakariki', 'floppy', 'fquestie',
            'carolune', 'johndbritton', 'stilettofiend', 'biscarri', 'netprogress', 'faisalchohan',
            'herblainchbury', 'annettestr', 'djmer1', 'jgarfunkel', 'brianacardysqa', 'davidsichinava',
            'arcanus_tco', 'mikeredding', 'dfg45', 'michael77', 'eirinipanou', 'michaljakob',
            'number9systems', 'goodonpharmi', 'nikolay', 'krisdev', 'derushi', 'no',
            'cheap', 'sssssssssssarah', 'francisds', 'josmasflores', 'replicatedtypo', 'pi2co',
            'catherinedem', 'jakubmracek', 'axel', 'papaioannoug', 'dcht00', 'timgluz',
            'eddankatz', 'psionjournal', 'business', 'billyb', 'valentinajanev', 'colinjojavin',
            'nightrose', 'jenit', 'juliamichlig', 'villavelius', 'qw12xy', 'atlasmuseum',
            'vannys', 'abdoulaye', 'gianel', 'antoniovangi', 'usa', 'darwin',
            'eysenbach', 'wart_dev', 'limikid', 'konko1974', 'desautomatas', 'antoniamelvin',
            'elaine', 'twittamood', 'bret_bernhoft', 'elenapasquini', 'higuerm', 'bgiwan',
            'lexcrsouza', 'macaia', 'enow', 'schubtom', 'newshack', 'insider230890',
            'fdf', 'sangeetab86', 'nerdvoid', 'josuegonzalez', 'open_ministry', 'evilgmonkey',
            'ghag', 'augustohp', 'darg', 'ermik', 'ou_com', 'cephillips',
            'loleg', 'tael67', 'behik', 'edward_gerth', 'arammxsdge', 'jfcosta',
            'eduardosantana', 'zy915617', 'raimondiand', 'dejaldir', 'love', 'namnamir',
            'kannappan', 'f', 'jucjsh', 'a_small_lab', 'robedemariage1111', 'wilbertboicexag',
            'turingcop', 'polyester', 'albert1t0', 'endecast', 'digibrum', 'kinlane',
            'phnk', 'playfairire', 'highmicro', 'paidicreed', 'sturlese', 'doclrogers',
            'seeyoujim', 'isiafrica', 'kinoraw', 'kajajacobsen', 'guille_perasso', 'landportal',
            'brian_root', 'jeannielir', 'jibolah', 'izhakbaruh', 'waijhet', 'kyyberi',
            'jararocha', 'sobookonline', 'mukruthi', 'monta', 'wilbanks', 'arturhoo',
            'nsartist34', 'citizensefeed', 'we', 'chaep', 'ok', 'nickblackbourn',
            'perfectlover09', 'tudiu', 'maiada', 'hspencer', 'techshaman', 'wunderkid',
            'any', 'nancy', 'societylink2', '163163', 'sdfas', 'leonardoruoso',
            'lexirodrigo', 'spoke', 'any', 'robertsonadams', 'erenmckay', 'theadamevans',
            'haklaekim', 'spiegro', 'thorkil', 'danicar', 'wolfgang8741', 'ghfgjfdf']