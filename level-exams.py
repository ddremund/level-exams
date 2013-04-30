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

import pymongo
import bottle
import questionDAO

@bottle.route('/')
def site_index():

	return questions.get_questions("", "1")

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)

database = connection.testing

questions = questionDAO.QuestionDAO(database)

bottle.run(host='leveling.rstnt.com', port=80)