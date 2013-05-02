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

	def insert_preference(self, name, value):

		print "Adding preference", name, value

		preference = {"name": name, "value": value}

		try:
			pref_id = self.preferences.insert(preference)
		except Exception, e:
			print "Error inserting preference:", e
			pref_id = None

		return pref_id

	def remove_preference(self, name):

		print "Removing preference", name

		try:
			removed = self.preferences.remove({"name": name})
		except Exception, e:
			print "Error removing preference:", e
			removed = 0

		return removed

	def get_preference(self, name):

		return self.preferences.find_one({"name": name})

	def get_all_preferences(self):

		cursor = self.preferences.find()
		return list(cursor)