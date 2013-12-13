# Google Apis
from google.appengine.api import users
from google.appengine.api.logservice import logservice
from webapp2_extras import sessions

# Custom importing
from base import BaseHandler
import schema

#
# Acts as the Frontpage when users are not signed in and the dashboard when they are.
# @author Johann du Toit
#
class HomepageHandler(BaseHandler):
	def get(self):

		# Locales
		locales = {
		}

		# Render the template
		self.render('main.html', locales)