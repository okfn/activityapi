#!/usr/bin/env python

import os
from lib.frontend import app

if __name__ == '__main__':
   port = int(os.environ.get('PORT', 5000))
   app.run(port=port, host='0.0.0.0')
