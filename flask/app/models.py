"""app/v1/users/models.py"""

from flask import jsonify, session


class User(object):

    def __init__(self):
        """ Initialize empty user list"""
        self.user_list = []
        self.notfound = None

    def create_user(self, user_name, user_phone, user_address):
        self.user_name = user_name
        self.user_phone = user_phone
        self.user_address =user_address

        if user not in user_list:
            self.user_list.append(self.user)

        return jsonify({ "new user created"}), 201

