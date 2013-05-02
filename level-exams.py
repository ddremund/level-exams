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
import savedTestDAO
import sessionDAO
import userDAO
import json
import cgi
import math
import re
import datetime
from random import shuffle

@bottle.route('/')
def site_index():

    # username = 'Derek'
    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        bottle.redirect("/login")

    return bottle.template('main_template', dict(username = username, 
        test_types = test_types.get_test_types()))

@bottle.get('/newquestion')
def get_newquestion():

    # username = 'Derek'
    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        bottle.redirect("/login")

    topics = set([question['topic'] for question in questions.get_all_questions()])

    return bottle.template('new_question', dict(username = username, topics = topics, 
        selected_topic = "", new_topic = "", errors = "", question = "", 
        answer = "", levels = [], image_urls = []))

@bottle.post('/newquestion')
def post_newquestion(): 

    #username = 'Derek'
    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        bottle.redirect("/login")

    topics = set([question['topic'] for question in questions.get_all_questions()])

    question = bottle.request.forms.get("question")
    answer = bottle.request.forms.get("answer")
    topic = bottle.request.forms.get("topic")
    new_topic = bottle.request.forms.get("new_topic")
    levels = bottle.request.forms.getall("level")
    image_urls = bottle.request.forms.get("image_urls").split(", ")

    if question == "" or answer == "" or topic == "" or len(levels) == 0 or (topic == "new" and new_topic == ""):
        errors = "Question must have question text, answer, topic, and associated levels."
        return bottle.template("new_question", dict(username = username, topics = topics, 
            selected_topic = topic, new_topic = new_topic, errors = errors, question = question, 
            answer = answer, levels = levels, image_urls = image_urls))
    
    escaped_question = question #cgi.escape(question, quote=True)
    escaped_answer = answer #cgi.escape(answer, quote=True)
    if topic == "new":
        escaped_topic = cgi.escape(new_topic, quote=True)
    else:
        escaped_topic = topic

    print "Inserting Question..."
    print "Topic:", escaped_topic
    print "Question:", escaped_question
    print "Answer:", escaped_answer
    print "Levels:", levels
    print "Image URLs:", image_urls
    questions.insert_question(escaped_topic, escaped_question, escaped_answer, 
        levels, image_urls)

    return bottle.template('new_question', dict(username = username, topics = topics, 
        selected_topic = "", new_topic = "", errors = "Question successfully inserted.", 
        question = "", answer = "", levels = [], image_urls = []))

@bottle.route('/question/remove/<question_id>')
def remove_question(question_id):

    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        bottle.redirect("/login")

    removed = questions.remove_question(question_id)
    bottle.redirect('/test/all')

@bottle.get('/question/<question_id>')
def get_editquestion(question_id):

    # username = 'Derek'
    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        bottle.redirect("/login")

    topics = set([question['topic'] for question in questions.get_all_questions()])
    question = questions.get_question(question_id)

    return bottle.template('edit_question', dict(username = username, topics = topics, 
        question_id = question['_id'], selected_topic = question['topic'], new_topic = "", errors = "", 
        question = question['question'], answer = question['answer'], levels = question['levels'],
        image_urls = question['image_urls']))

@bottle.post('/question/<question_id>')
def post_editquestion(question_id):

    # username = 'Derek'
    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        bottle.redirect("/login")

    topics = set([question['topic'] for question in questions.get_all_questions()])
    question = bottle.request.forms.get("question")
    answer = bottle.request.forms.get("answer")
    topic = bottle.request.forms.get("topic")
    new_topic = bottle.request.forms.get("new_topic")
    levels = bottle.request.forms.getall("level")
    image_urls = bottle.request.forms.get("image_urls").split(", ")

    if question == "" or answer == "" or topic == "" or len(levels) == 0 or (topic == "new" and new_topic == ""):
        errors = "Question must have question text, answer, topic, and associated levels."
        return bottle.template("edit_question", dict(username = username, topics = topics, 
            question_id = question_id, selected_topic = topic, new_topic = new_topic, 
            errors = errors, question = question, answer = answer, levels = levels, image_urls = image_urls))

    escaped_question = question#cgi.escape(question, quote=True)
    escaped_answer = answer#cgi.escape(answer, quote=True)
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
    print "Image URLs:", image_urls
    questions.update_question(question_id, escaped_topic, escaped_question, escaped_answer, levels, image_urls)

    errors = "Question successfully updated."
    return bottle.template("edit_question", dict(username = username, topics = topics, 
            question_id = question_id, selected_topic = topic, new_topic = new_topic, 
            errors = errors, question = question, answer = answer, levels = levels, image_urls = image_urls))

@bottle.route('/test/all')
def create_test_all():

    #username = 'Derek'
    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        bottle.redirect("/login")

    timestamp = str(datetime.datetime.now()).split('.')[0]
    description = "All Questions"
    level = 3
    pct_top = 100

    test_questions = {}
    topics = set([question['topic'] for question in questions.get_all_questions()])

    for topic in topics:
        topic_questions = []
        for level in [1,2,3]:
            topic_questions.extend(questions.get_questions(topic, str(level)))
        # uniquify questions
        test_questions[topic] = {q['_id']:q for q in topic_questions}.values()

        test_questions[topic].sort(key= lambda item: min(item['levels']))

    return bottle.template('test_template', dict(username = username, 
        description = description, pct_top = pct_top, level = "All",
        test_id = "not applicable", questions = test_questions, 
        timestamp = timestamp))

@bottle.get('/test/custom')
def get_test_custom():

    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        bottle.redirect("/login")

    topics = set([question['topic'] for question in questions.get_all_questions()])

    return bottle.template("custom_test", dict(username = username, errors = "", 
        name = "", pct_lower = "", selected_level = "", topics = topics))

@bottle.post('/test/custom')
def post_test_custom():

    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        bottle.redirect("/login")

    topics = set([question['topic'] for question in questions.get_all_questions()])

    name = bottle.request.forms.get("name")
    pct_lower = bottle.request.forms.get("pct_lower")
    dest_level = bottle.request.forms.get("dest_level")

    if name == "" or pct_lower == "" or dest_level == "":
        errors = "Custom test must have values for all options."
        return bottle.template("custom_test", dict(username = username, errors = errors, 
            name = name, pct_lower = pct_lower, selected_level = dest_level, topics = topics))

    topic_counts = {}
    for topic in topics:
        topic_counts[topic] = int(bottle.request.forms.get(topic))

    print "Inserting custom test..."
    template_id = test_types.insert_test_type(name, 100 - int(pct_lower), int(dest_level), topic_counts)

    bottle.redirect('/test/{}'.format(template_id))

@bottle.route('/test/remove/<template_id>')
def remove_test(template_id):

    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        bottle.redirect("/login")

    removed = test_types.remove_test_type(template_id)
    bottle.redirect('/')


@bottle.route('/test/<template_id>')
def create_test(template_id):

    #username = 'Derek'
    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        bottle.redirect("/login")

    test_type = test_types.get_test_type(cgi.escape(template_id))

    print "Generating test..."
    print "Template ID:", template_id
    print "Type:", test_type

    test_questions = {}

    timestamp = str(datetime.datetime.now()).split('.')[0]
    description = test_type['name']
    level = test_type['dest_level']
    pct_top = test_type['pct_top_level']
    topics = test_type['topic_counts']

    for topic in topics.keys():
        level_questions = questions.get_questions(topic, str(level))
        shuffle(level_questions)
        topic_questions = level_questions[0:int(math.ceil(pct_top / 100.0 * topics[topic]))]
        dup_ids = [question["_id"] for question in topic_questions]
        level_questions = questions.get_questions(topic, str(int(level) - 1), 0, dup_ids)
        shuffle(level_questions)
        topic_questions.extend(level_questions[0:int(math.ceil((1 - pct_top / 100.0) * topics[topic]))])
        test_questions[topic] = topic_questions
        test_questions[topic].sort(key= lambda item: min(item['levels']))
        print topic, len(topic_questions)
        
    saved_test_id = saved_tests.insert_test(username, description, level, 
                                            pct_top, test_questions, timestamp)

    return bottle.template('test_template', dict(username = username, 
        description = description, pct_top = pct_top, level = level,
        questions = test_questions, test_id = saved_test_id, 
        timestamp = timestamp))

@bottle.route('/test/saved/<test_id>')
def retrieve_test(test_id):

    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        bottle.redirect("/login")

    test = saved_tests.get_test(test_id)

    return bottle.template('test_template', dict(username = test['username'],
        description = test['template'], pct_top = test['pct_top'], 
        level = test['level'], questions = test['questions'], 
        test_id = test_id, timestamp = test['timestamp']))

@bottle.route('/test/saved/all')
def retrieve_all_tests():

    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    if username is None:
        bottle.redirect("/login")

    tests = saved_tests.get_all_tests()
    tests.sort(key = lambda item: item['timestamp'])

    return bottle.template('saved_tests', dict(username = usersname, 
                                            tests = tests))

@bottle.get('/internal_error')
@bottle.view('error_template')
def present_internal_error():
    return {'error':"System has encountered a DB error"}

# displays the initial signup form
@bottle.get('/signup')
def present_signup():
    return bottle.template("signup",
                           dict(username="", password="",
                                password_error="",
                                email="", username_error="", email_error="",
                                verify_error =""))

# displays the initial login form
@bottle.get('/login')
def present_login():
    return bottle.template("login",
                           dict(username="", password="",
                                login_error=""))

@bottle.post('/login')
def process_login():

    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")

    print "user submitted ", username, "pass ", password

    user_record = users.validate_login(username, password)
    if user_record:
        # username is stored in the user collection in the _id key
        session_id = sessions.start_session(user_record['_id'])

        if session_id is None:
            bottle.redirect("/internal_error")

        cookie = session_id

        # Warning, if you are running into a problem whereby the cookie being set here is
        # not getting set on the redirect, you are probably using the experimental version of bottle (.12).
        # revert to .11 to solve the problem.
        bottle.response.set_cookie("session", cookie)

        bottle.redirect("/")

    else:
        return bottle.template("login",
                               dict(username=cgi.escape(username), password="",
                                    login_error="Invalid Login"))

@bottle.get('/logout')
def process_logout():

    cookie = bottle.request.get_cookie("session")

    sessions.end_session(cookie)

    bottle.response.set_cookie("session", "")


    bottle.redirect("/login")

@bottle.post('/signup')
def process_signup():

    signup_enabled = True

    if signup_enabled == False:
        bottle.redirect("/")

    email = bottle.request.forms.get("email")
    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")
    verify = bottle.request.forms.get("verify")

    # set these up in case we have an error case
    errors = {'username': cgi.escape(username), 'email': cgi.escape(email)}
    if validate_signup(username, password, verify, email, errors):

        if not users.add_user(username, password, email):
            # this was a duplicate
            errors['username_error'] = "Username already in use. Please choose another"
            return bottle.template("signup", errors)

        session_id = sessions.start_session(username)
        print session_id
        bottle.response.set_cookie("session", session_id)
        bottle.redirect("/")
    else:
        print "user did not validate"
        return bottle.template("signup", errors)


# validates that the user information is valid for new signup, return True of False
# and fills in the error string if there is an issue
def validate_signup(username, password, verify, email, errors):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    PASS_RE = re.compile(r"^.{3,20}$")
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

    errors['username_error'] = ""
    errors['password_error'] = ""
    errors['verify_error'] = ""
    errors['email_error'] = ""

    if not USER_RE.match(username):
        errors['username_error'] = "invalid username. try just letters and numbers"
        return False

    if not PASS_RE.match(password):
        errors['password_error'] = "invalid password."
        return False
    if password != verify:
        errors['verify_error'] = "password must match"
        return False
    if email != "":
        if not EMAIL_RE.match(email):
            errors['email_error'] = "invalid email address"
            return False
    return True

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)

database = connection.leveling

questions = questionDAO.QuestionDAO(database)
test_types = testTypeDAO.TestTypeDAO(database)
saved_tests = savedTestDAO.SavedTestDAO(database)
users = userDAO.UserDAO(database)
sessions = sessionDAO.SessionDAO(database)

#bottle.debug(True)
bottle.run(host='leveling.rstnt.com', port=80)