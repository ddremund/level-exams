#!/usr/bin/python -tt

# Copyright 2013 Derek Remund (derek.remund@rackspace.com)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from bson.objectid import ObjectId

class PreferenceDAO:

	def __init__(self, database):

		self.db = database
		self.preferences = database.preferences

	def set_preference(self, name, value):

		print "Updating preference", name, value

		try:
			pref_id = self.preferences.update({'_id': 'master'}, {'$set': {'{}'.format(name): value}}, True)
		except Exception, e:
			print "Error updating preference:", e
			pref_id = None

		return pref_id

	def remove_preference(self, name):

		print "Removing preference", name

		try:
			pref_id = self.preferences.update({'_id': 'master'}, {'$unset': {'{}'.format(name): 1}})
		except Exception, e:
			print "Error removing preference:", e
			pref_id = None

		return pref_id

	def get_preference(self, name):

		master_prefs = self.preferences.find_one({"_id": 'master'}, {'_id': 0})
		return master_prefs[name]

	def get_master_preferences(self):

		master_prefs = self.preferences.find_one({'_id': 'master'})
		if master_prefs is None:
			master_prefs = {}
		return master_prefs