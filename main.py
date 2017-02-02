#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r".{3,20}$")
VERIFY_RE= re.compile(r".{3,20}$")
EMAIL_RE= re.compile(r"[\S]+@[\S]+.[\S]+$")
page_header="""
<!DOCTYPE html>
<html>
<head>
    <title>
    User Signup.
    </title>
</head>
<body>
    <h1>
    User signup!
    </h1>

"""
page_footer="""
</body>
</html>
"""
initial_params={'username':"", 'email':"",'error_username':"",'error_password':"",'error_verify':"",'error_email':""}

user_form= """<form action="/sign-up" method="post">
    <label for="username">
        Username: <input name="username" type="text" value= {username}>
    </label>
        <div class= "error" style="color: red">{error_username}</div>
    <br>
    <label for="password">
        Password: <input name="password" type="password" required/>
    </label>
        <div class= "error" style="color: red">{error_password}</div>
    <br>
    <label for="verify">
        Verify Password: <input name="verify" type="password" required />
    </label>
        <div class= "error" style="color: red">{error_verify}</div>
    <br>
    <label for="email">
        Email (optional): <input name="email" type="email" value={email}>
    </label>
        <div class= "error" style="color: red">{error_email}</div>
    <p><input type='submit' value='Sign in!'/></p>
    """


def valid_username(username):
    if username and USER_RE.match(username):
        return True
    else:
        return False
def valid_password(password):
    if password and PASS_RE.match(password):
        return True
    else:
        return False
def valid_verify(verify):
    if verify and VERIFY_RE.match(verify):
        return True
    else:
        return False
def valid_email(email):
    if not email or EMAIL_RE.match(email):
        return True
    else:
        return False


class Index(webapp2.RequestHandler):

    def get(self):


        content=page_header+user_form.format(**initial_params)+page_footer
        self.response.write(content)




class Signup(webapp2.RequestHandler):
    def post(self):

        error=""
        have_error=False
        username=self.request.get('username')
        password=self.request.get('password')
        verify=self.request.get('verify')
        email=self.request.get('email')
        params={"username": username, "email":email}
        if not valid_username(username):
            have_error=True
            params["error_username"]="That's not a valid username."
        else:
            params["error_username"]=""


        if not valid_password(password):
            have_error=True
            params["error_password"]="That's not a valid password."
        else:
            params["error_password"]=""

        if not valid_verify(str(verify)):
            have_error=True
            params["error_verify"]=""

        elif password!=verify:
            have_error=True
            params["error_verify"]="Password's don't match."
        else:
            params["error_verify"]=""


        if  valid_email(email)==False:
            have_error=True
            params["error_email"]="That's not a valid email"
        else:
            params["error_email"]=""

        if have_error==True:
            content=page_header+user_form.format(**params)+page_footer
            self.response.write(content)

        else:
            content="Welcome "+username
            self.response.write(content)







app = webapp2.WSGIApplication([
    ('/', Index),
    ('/sign-up', Signup)

], debug=True)
