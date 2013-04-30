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

class TestTypeDAO:

	def __init__(self, database):

		self.db = database
		self.test_types = database.test_types

	def insert_test_type(self, name):

		print "Inserting Test Type", name

		test_type = {"name": name}

		try:
			self.test_types.insert(test_type)
		except Exception, e:
			print "Error inserting post:", e

	def get_test_types(self):

		results = []
		cursor = self.test_types.find()
		for test_type in cursor:
			results.append({"name": test_type["name"]})
		return results