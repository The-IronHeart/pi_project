#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/pi/pi_project/")

from pi_project import app as application
from pi_project import Config
application.secret_key = Config.secret_key 