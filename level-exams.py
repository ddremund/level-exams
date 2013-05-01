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
import testTypeDAO
import json
import cgi
import math

@bottle.route('/')
def site_index():

	username = 'Derek'

	return bottle.template('main_template', dict(username = username, 
		test_types = test_types.get_test_types()))

@bottle.get('/newquestion')
def get_newquestion():

	username = 'Derek'

	topics = set([question['topic'] for question in questions.get_all_questions()])

	return bottle.template('new_question', dict(username = username, topics = topics, 
		selected_topic = "", new_topic = "", errors = "", question = "", answer = "", levels = []))

@bottle.post('/newquestion')
def post_newquestion():	

	username = 'Derek'

	topics = set([question['topic'] for question in questions.get_all_questions()])

	question = bottle.request.forms.get("question")
	answer = bottle.request.forms.get("answer")
	topic = bottle.request.forms.get("topic")
	new_topic = bottle.request.forms.get("new_topic")
	levels = bottle.request.forms.getall("level")

	if question == "" or answer == "" or topic == "" or len(levels) == 0 or (topic == "new" and new_topic == ""):
		errors = "Question must have question text, answer, topic, and associated levels."
		return bottle.template("new_question", dict(username = username, topics = topics, 
			selected_topic = topic, new_topic = new_topic, errors = errors, question = question, 
			answer = answer, levels = levels))
	
	escaped_question = cgi.escape(question, quote=True)
	escaped_answer = cgi.escape(answer, quote=True)
	if topic == "new":
		escaped_topic = cgi.escape(new_topic, quote=True)
	else:
		escaped_topic = topic

	print "Inserting Question..."
	print "Topic:", escaped_topic
	print "Question:", escaped_question
	print "Answer:", escaped_answer
	print "Levels:", levels
	questions.insert_question(escaped_topic, escaped_question, escaped_answer, levels)

	return bottle.template('new_question', dict(username = username, topics = topics, 
		selected_topic = "", new_topic = "", errors = "Question successfully inserted.", 
		question = "", answer = "", levels = []))

@bottle.get('/question/<question_id>')
def get_editquestion(question_id):

	username = 'Derek'

	topics = set([question['topic'] for question in questions.get_all_questions()])
	question = questions.get_question(question_id)

	return bottle.template('edit_question', dict(username = username, topics = topics, 
		question_id = question['_id'], selected_topic = question['topic'], new_topic = "", errors = "", 
		question = question['question'], answer = question['answer'], levels = question['levels']))

@bottle.post('/question/<question_id>')
def post_editquestion(question_id):
	username = 'Derek'

	topics = set([question['topic'] for question in questions.get_all_questions()])
	question = bottle.request.forms.get("question")
	answer = bottle.request.forms.get("answer")
	topic = bottle.request.forms.get("topic")
	new_topic = bottle.request.forms.get("new_topic")
	levels = bottle.request.forms.getall("level")

	if question == "" or answer == "" or topic == "" or len(levels) == 0 or (topic == "new" and new_topic == ""):
		errors = "Question must have question text, answer, topic, and associated levels."
		return bottle.template("edit_question", dict(username = username, topics = topics, 
			question_id = question_id, selected_topic = topic, new_topic = new_topic, 
			errors = errors, question = question, answer = answer, levels = levels))

	escaped_question = cgi.escape(question, quote=True)
	escaped_answer = cgi.escape(answer, quote=True)
	if topic == "new":
		escaped_topic = cgi.escape(new_topic, quote=True)
	else:
		escaped_topic = topic

	print "Updating Question..."
	print "_id:", question_id
	print "Topic:", escaped_topic
	print "Question:", escaped_question
	print "Answer:", escaped_answer
	print "Levels:", levels
	questions.update_question(question_id, escaped_topic, escaped_question, escaped_answer, levels)

	errors = "Question successfully updated."
	return bottle.template("edit_question", dict(username = username, topics = topics, 
			question_id = question_id, selected_topic = topic, new_topic = new_topic, 
			errors = errors, question = question, answer = answer, levels = levels))

@bottle.route('/test/all')
def create_test_all():

	username = 'Derek'

	description = "All Questions"
	level = 3
	pct_top = 100

	test_questions = {}
	topics = set([question['topic'] for question in questions.get_all_questions()])

	for topic in topics:
		topic_questions = []
		for level in [1,2,3]:
			topic_questions.extend(questions.get_questions(topic, str(level)))
		test_questions[topic] = {q['_id']:q for q in topic_questions}.values()

	return bottle.template('test_template', dict(username = username, 
		description = description, pct_top = pct_top, 
		questions = test_questions))

@bottle.route('/test/<test_id>')
def create_test(test_id):

	username = 'Derek'
	test_type = test_types.get_test_type(cgi.escape(test_id))

	print "Generating test..."
	print "Test ID:", test_id
	print "Type:", test_type

	test_questions = {}

	description = test_type['name']
	level = test_type['dest_level']
	pct_top = test_type['pct_top_level']
	topics = test_type['topic_counts']

	for topic in topics.keys():
		topic_questions = questions.get_questions(topic, str(level), 
						int(math.ceil(pct_top / 100.0 * topics[topic])))
		dup_ids = [question["_id"] for question in topic_questions]
		if int(level) > 1:
			topic_questions.extend(questions.get_questions(topic, str(int(level) - 1), 
				int(math.ceil((1 - pct_top / 100.0) * topics[topic])), dup_ids))
		test_questions[topic] = topic_questions

		print topic, len(topic_questions)


	return bottle.template('test_template', dict(username = username, 
		description = description, pct_top = pct_top, 
		questions = test_questions))

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)

database = connection.testing

questions = questionDAO.QuestionDAO(database)
test_types = testTypeDAO.TestTypeDAO(database)

bottle.run(host='localhost', port=80)