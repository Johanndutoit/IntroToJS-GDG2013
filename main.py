#!/usr/bin/env python

# Python Libs
import webapp2
from webapp2_extras import routes
import jinja2
import os
import urllib

# Setup the Handlers
from handlers.home import HomepageHandler
from handlers.endpoints import EndpointsHandler
from handlers.admin import ListAllEndpointHandler, HandleSave, HandleDelete

# General Config for our web application
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'secret_key_for_session_here',
}

# Startup our app with the routes we are
# going to configure now
app = webapp2.WSGIApplication([

	('/', HomepageHandler),
	('/endpoints', EndpointsHandler),
	('/admin', ListAllEndpointHandler),
	('/admin/save', HandleSave),
	('/admin/delete', HandleDelete)

], debug=True, config=config)