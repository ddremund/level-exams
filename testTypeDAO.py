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

class TestTypeDAO:

	def __init__(self, database):

		self.db = database
		self.test_types = database.test_types

	def insert_test_type(self, name, pct_top_level, dest_level, topic_counts):

		print "Inserting Test Type", name

		test_type = {"name": name,
					 "dest_level": dest_level,
					 "pct_top_level": pct_top_level,
					 "topic_counts": topic_counts}

		try:
			test_id = self.test_types.insert(test_type)
		except Exception, e:
			print "Error inserting test type:", e
			test_id = None

		return test_id

	def remove_test_type(self, type_id):

		print "Removing Test Type", type_id

		try:
			removed = self.test_types.remove({"_id": ObjectId(type_id)})
		except Exception, e:
			print "Error removing test type:", e
			removed = 0

		return removed

	def get_test_types(self):

		cursor = self.test_types.find()
		return list(cursor)

	def get_test_type(self, type_id):

		return self.test_types.find_one({'_id': ObjectId(type_id)})