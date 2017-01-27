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
def build_page(page_content):
    user_form= """
        <form action="/signup" method="post">
            <label for="username">
                Username: <input name="username" type="text" value required/>
            </label><br>
            <label for="password">
                Password: <input name="password" type="password" value required/>
            </label><br>
            <label for="verify">
                Verify Password: <input name="verify" type="password" value required/>
            </label><br>
            <label for="email">
                Email (optional): <input name="email" type="email" value/>
            </label>

    """
    content=page_header+user_form+page_footer
    return (content)
def username_check(user_name):
    username=str(user_name)
    if username=="":
        error="You didn't enter a username."
        error_escaped=cgi.escape(error,quote=True)
        self.redirect("/?error=" + error_escaped)
    for a in username

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content=build_page("")
        self.response.write(content)

class SignUp(webapp2.RequestHandler):
    def post(self):
        new_user=self.response.get('username')
        new_password=self.response.get('password')
        new_verify=self.response.get('verify')
        new_email=self.response.get('email')




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/signup',SignUp)
], debug=True)
