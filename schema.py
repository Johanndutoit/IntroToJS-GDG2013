# Google Libraries
from google.appengine.ext import ndb

#
# Event Details
# @author Johann du Toit
#
class Endpoint(ndb.Model):
	title = ndb.StringProperty()
	lat = ndb.StringProperty(default=None)
	lng = ndb.StringProperty(default=None)
	icon = ndb.StringProperty(default=None)
	created = ndb.DateTimeProperty(auto_now_add=True)
	lastupdated = ndb.DateTimeProperty(auto_now_add=True,auto_now=True)

	#
	# Checks and returns the account_obj for that
	# provider
	#
	@staticmethod
	def get_single_result(query_obj):

		# Get all the accounts with that limit
		item_objs = query_obj.fetch(limit=1)

		# Did we get a account ?
		if item_objs != None and len(item_objs) > 0:

			# Return the first
			return item_objs[0]

		else:

			# Else this is a false request
			return False
