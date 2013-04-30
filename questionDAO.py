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

class QuestionDAO:

	def __init__(self, database):

		self.db = database
		self.questions = database.questions

	def insert_question(self, topic, question, answer, levels_array):

		print "Inserting question", topic, question, answer, levels_array

		question = {"topic": topic, 
					"question": question,
					"answer": answer,
					"levels": levels_array}

		try:
			self.questions.insert(question)
		except Exception, e:
			print "Error inserting post:", e

	def get_questions(self, category, level, num_questions = 0):

		if num_questions == 0:
			result = self.questions.find()
		else:
			result = self.questions.find().limit(num_questions)

		return result