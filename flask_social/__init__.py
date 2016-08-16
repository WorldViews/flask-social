# -*- coding: utf-8 -*-
"""
    flask.ext.social
    ~~~~~~~~~~~~~~~~

    Flask-Social is a Flask extension that aims to add simple OAuth provider
    integration for Flask-Security

    :copyright: (c) 2012 by Matt Wright.
    :license: MIT, see LICENSE for more details.
"""

print 5 * (60*"*"+"\n") + (60*"*")
print "This ugly message comes from flask_social/__init__.py"
print 6 * (60*"*"+"\n")

__version__ = '1.6.2'

from .core import Social
from .datastore import SQLAlchemyConnectionDatastore, \
     MongoEngineConnectionDatastore, PeeweeConnectionDatastore
from .signals import connection_created, connection_failed, login_failed, \
     connection_removed, login_completed
