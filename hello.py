# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pprint
import sys
from apiclient.discovery import build
import urllib2
import simplejson
import pprint


# For this example, the API key is provided as a command-line argument.
api_key = sys.argv[1]

# The apiclient.discovery.build() function returns an instance of an API service
# object that can be used to make API calls. The object is constructed with
# methods specific to the books API. The arguments provided are:
#   name of the API ('books')
#   version of the API you are using ('v1')
#   API key
service = build('books', 'v1', developerKey=api_key)

# The books API has a volumes().list() method that is used to list books
# given search criteria. Arguments provided are:
#   volumes source ('public')
#   search query ('android')
# The method returns an apiclient.http.HttpRequest object that encapsulates
# all information needed to make the request, but it does not call the API.
request = service.volumes().list(source='public',projection='lite', q='network',maxResults=4)
# The execute() function on the HttpRequest object actually calls the API.
# It returns a Python object built from the JSON response. You can print this
# object or refer to the Books API documentation to determine its structure.
respon = request.execute()
#print(response)
#pprint.pprint(respon)
booksnames=[] #initialisong a list obj in python

authorlist=[]
k='%3A'
# Accessing the response like a dict object with an 'items' key returns a list
# of item objects (books). The item object is a dict object with a 'volumeInfo'
# key. The volumeInfo object is a dict with keys 'title' and 'authors'.
# print 'Found %d books:' % len(response['items'])
for book in respon.get('items', []):
  		#print 'Title: %s, Authors: %s' % ( book['volumeInfo']['title'],book['volumeInfo']['authors'])
  		
  		booksnames.append(book['volumeInfo']['title'])      #list appending in python
  		authorlist.append(book['volumeInfo']['authors'])
  		#print 'hello'
  		#print "Value : %s" %  book.items()
  		#print "Value : %s" %  book.keys()
  		
for i in booksnames: #(for looping iin python )
 	print i
 
for i in booksnames:
	i=i.replace(" ","%20")

	
	url = ('https://ajax.googleapis.com/ajax/services/search/web'
       '?v=1.0&q=%s' % i+'%3Apdf&userip=USERS-IP-ADDRESS' )
	print url
	request = urllib2.Request(
  		  url, None)

	response = urllib2.urlopen(request)
	print response
# 	i=0	
# 	# Process the JSON string.
# 	result = simplejson.load(response)
# 	f=len(result['responseData']['results'])
# #pprint.pprint(result)
# 	while f>2:
#   	 #print 'Title: %s' % ( book['results']['title'])
#  	 #print 'hello'
# 		print result['responseData']['results'][f-1]['url']
#  		f=f-1

