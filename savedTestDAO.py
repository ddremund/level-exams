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

class SavedTestDAO:

	def __init__(self, database):

		self.db = database
		self.saved_tests = database.saved_tests

	def insert_test(self, username, description, level, pct_top, questions):

		print "Saving test"

		test = {"username": username,
				"template": description,
				"level": level,
				"pct_top": pct_top, 
				"questions": questions}

		try:
			test_id = self.saved_tests.insert(test)
		except Exception, e:
			print "Error saving test:", e
			test_id = None

		return test_id

	def remove_test(self, test_id):

		print "Removing test", test_id

		try:
			removed = self.questions.remove({"_id": ObjectId(test_id)})
		except Exception, e:
			print "Error removing test:", e
			removed = 0

		return removed

	def get_test(self, test_id):

		return self.saved_tests.find_one({"_id": ObjectId(test_id)})

	def get_all_tests(self):

		cursor = self.saved_tests.find()
		return list(cursor)