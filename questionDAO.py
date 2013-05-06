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

class QuestionDAO:

	def __init__(self, database):

		self.db = database
		self.questions = database.questions

	def insert_question(self, topic, question, answer, levels_array, image_urls = []):

		print "Inserting question", topic, question, answer, levels_array, image_urls

		question = {"topic": topic, 
					"question": question,
					"answer": answer,
					"levels": levels_array,
					"image_urls": image_urls}

		try:
			question_id = self.questions.insert(question)
		except Exception, e:
			print "Error inserting post:", e
			question_id = None

		return question_id

	def remove_question(self, question_id):

		print "Removing Question", question_id

		try:
			removed = self.questions.remove({"_id": ObjectId(question_id)})
		except Exception, e:
			print "Error removing question:", e
			removed = 0
			
		return removed

	def update_question(self, question_id, topic, question, answer, levels_array, image_urls = []):

		print "Updating question", question_id

		question = {"_id": ObjectId(question_id),
					"topic": topic,
					"question": question,
					"answer": answer,
					"levels": levels_array,
					"image_urls": image_urls}

		try:
			updated = self.questions.update({"_id": ObjectId(question_id)}, question)
		except Exception, e:
			print "Error upating question:", e
			updated = None

		return updated

	def get_question(self, question_id):

		return self.questions.find_one({"_id": ObjectId(question_id)})

	def get_questions_for_topic(self, topic):

		cursor = self.questions.find({"topic": topic})
		return list(cursor)

	def get_questions(self, topic, level, num_questions = 0, dup_ids = []):

		dup_ids = [ObjectId(id) for id in dup_ids]
		if num_questions == 0:
			cursor = self.questions.find({"topic": topic, "levels": level})
		else:
			cursor = self.questions.find({"topic": topic, "levels": level, "_id": {"$nin": dup_ids}}).limit(num_questions)

		return list(cursor)

	def get_all_questions(self):

		cursor = self.questions.find()
		return list(cursor)
