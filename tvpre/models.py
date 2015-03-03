from google.appengine.ext import ndb

# We set a parent key on the 'Greetings' to ensure that they are all in the same
# entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.

class UserDict(ndb.Model):
    user_id = ndb.StringProperty()
    string_dict = ndb.JsonProperty()
