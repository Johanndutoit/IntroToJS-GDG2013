 # Google Apis
from google.appengine.api import users
from google.appengine.api.logservice import logservice
from webapp2_extras import sessions

# Custom importing
from base import BaseHandler
import json
import schema

#
# Acts as the Frontpage when users are not signed in and the dashboard when they are.
# @author Johann du Toit
#
class ListAllEndpointHandler(BaseHandler):
	def get(self):

		# Locales
		locales = {

			'endpoint_objs': schema.Endpoint.query().fetch()

		}

		# Render the template
		self.render('admin_list.html', locales)

#
# Acts as the Frontpage when users are not signed in and the dashboard when they are.
# @author Johann du Toit
#
class HandleDelete(BaseHandler):

	def post(self):

		id_str = self.request.POST.get('id')

		endpoint_obj = schema.Endpoint.get_by_id(long(id_str))
		print endpoint_obj
		if endpoint_obj != None:
			endpoint_obj.key.delete()
		self.response.out.write('done')

#
# Acts as the Frontpage when users are not signed in and the dashboard when they are.
# @author Johann du Toit
#
class HandleSave(BaseHandler):

	def post(self):

		title = self.request.POST.get('title')
		id_str = self.request.POST.get('id')
		lat = self.request.POST.get('lat')
		lng = self.request.POST.get('lng')
		icon = self.request.POST.get('icon')

		endpoint_obj = schema.Endpoint()

		if id_str != None:
			endpoint_obj = schema.Endpoint.get_by_id(long(id_str))

		endpoint_obj.title = title
		endpoint_obj.lat = lat
		endpoint_obj.lng = lng
		endpoint_obj.icon = icon
		endpoint_obj.put()
		self.response.out.write('done')




