# Google Apis
from google.appengine.api import users
from google.appengine.api.logservice import logservice
from webapp2_extras import sessions

# Custom importing
from base import BaseHandler
import schema
import json

#
# Acts as the Frontpage when users are not signed in and the dashboard when they are.
# @author Johann du Toit
#
class EndpointsHandler(BaseHandler):
	def get(self):

		endpoint_objs = schema.Endpoint.query().fetch()
		endpoint_obs = []

		for end in endpoint_objs:
			endpoint_obs.append({

				'title': end.title,
				'lat': end.lat,
				'lng': end.lng,
				'icon': end.icon,
				'id': end.key.id()

			})

		# Locales
		self.response.out.write( json.dumps( endpoint_obs ) )