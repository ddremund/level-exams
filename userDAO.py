

#
# Copyright (c) 2008 - 2013 10gen, Inc. <http://10gen.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
import hmac
import random
import string
import hashlib
import pymongo


# The User Data Access Object handles all interactions with the User collection.
class UserDAO:

    def __init__(self, db):
        self.db = db
        self.users = self.db.users
        self.SECRET = 'verysecret'

    # makes a little salt
    def make_salt(self):
        salt = ""
        for i in range(5):
            salt = salt + random.choice(string.ascii_letters)
        return salt

    # implement the function make_pw_hash(name, pw) that returns a hashed password
    # of the format:
    # HASH(pw + salt),salt
    # use sha256

    def make_pw_hash(self, pw,salt=None):
        if salt == None:
            salt = self.make_salt();
        return hashlib.sha256(pw + salt).hexdigest()+","+ salt

    # Validates a user login. Returns user record or None
    def validate_login(self, username, password):

        user = None
        try:
            user = self.users.find_one({'_id': username})
        except:
            print "Unable to query database for user"

        if user is None:
            print "User not in database"
            return None

        salt = user['password'].split(',')[1]

        if user['password'] != self.make_pw_hash(password, salt):
            print "user password is not a match"
            return None

        # Looks good
        return user


    # creates a new user in the users collection
    def add_user(self, username, password, email, roles = []):
        password_hash = self.make_pw_hash(password)

        user = {'_id': username, 'password': password_hash, 'roles': roles}
        if email != "":
            user['email'] = email

        print "Creating user", username
        try:
            self.users.insert(user, safe=True)
        except pymongo.errors.OperationFailure:
            print "oops, mongo error"
            return False
        except pymongo.errors.DuplicateKeyError as e:
            print "oops, username is already taken"
            return False

        return True

    def remove_user(self, username):

        print "Removing user", username

        try:
            self.users.remove({'_id': username})
        except Exception, e:
            print 'Error removing user:', e
            return False

        return True

    def change_password(self, username, password):

        password_hash = self.make_pw_hash(password)

        try:
            self.users.update({'_id': username}, 
                {'$set': {'password': password_hash}})
        except Exception, e:
            print "Error updating password", e
            return "Error changing password"
        else:
            return "Password successfully changed"

    def get_roles(self, username):

        return self.users.find_one({'_id': username}, {'roles': 1, '_id': 0})['roles']

    def set_roles(self, username, roles):

        return self.users.update({'_id': username}, {'$set': {'roles': roles}})

    def get_all_users(self):

        cursor = self.users.find()
        return sorted(list(cursor), key = lambda item: item["_id"])
