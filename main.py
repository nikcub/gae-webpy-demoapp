#!/usr/bin/env python
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import util
from models import *
import web

# define your routes
#
# Note: you can use either app.yaml or web.py to route your requests
# how you do this is up to you. Here we have a catch-all for all dynamic
# requests landing here. 

routes = (
  '/', 'index',
  '/item(*.)', 'item_handler'
)

render = web.template.render('templates', base='base')

class index:
	def GET(self):
		items = TodoItem.all()
		userinfo = users.get_current_user()
		return render.index(items, userinfo, users)
		
	def POST(self):
		i = web.input()
		item = TodoItem()

		user = users.get_current_user()

		if user:
			item.author = user

		item.content = i.content
		item.put()
		return web.seeother('/')
		
	def user_info(self):
		user = users.get_current_user()


class item_handler:
	def POST(self, var):
		i = web.input()


def main():
	app = web.application(routes, globals())
	main = app.cgirun()

if __name__ == '__main__':
    main()