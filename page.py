#!/usr/bin/env python
# coding=utf-8

import os
import datetime
import random

from google.appengine.ext import webapp
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

from v2ex.babel import Member
from v2ex.babel import Counter
from v2ex.babel import Section
from v2ex.babel import Node
from v2ex.babel import Topic
from v2ex.babel import Reply
from v2ex.babel import Site

from v2ex.babel.security import *
from v2ex.babel.ua import *
from v2ex.babel.da import *
from v2ex.babel.ext.cookies import Cookies

template.register_template_library('v2ex.templatetags.filters')

class AboutHandler(webapp.RequestHandler):
    def get(self):
        site = GetSite()
        template_values = {}
        template_values['site'] = site
        template_values['rnd'] = random.randrange(1, 100)
        note = GetKindByNum('Note', 127)
        if note is False:
            note = GetKindByNum('Note', 1)
        template_values['note'] = note
        member = CheckAuth(self)
        if member:
            template_values['member'] = member
        template_values['page_title'] = site.title + u' › About'
        path = os.path.join(os.path.dirname(__file__), 'tpl', 'desktop', 'about.html')
        output = template.render(path, template_values)
        self.response.out.write(output)
        
class FAQHandler(webapp.RequestHandler):
    def get(self):
        site = GetSite()
        template_values = {}
        template_values['site'] = site
        template_values['rnd'] = random.randrange(1, 100)
        note = GetKindByNum('Note', 195)
        if note is False:
            note = GetKindByNum('Note', 3)
        template_values['note'] = note
        member = CheckAuth(self)
        if member:
            template_values['member'] = member
        template_values['page_title'] = site.title + u' › FAQ'
        path = os.path.join(os.path.dirname(__file__), 'tpl', 'desktop', 'faq.html')
        output = template.render(path, template_values)
        self.response.out.write(output)

class PlanHandler(webapp.RequestHandler):
    def get(self):
        site = GetSite()
        template_values = {}
        template_values['site'] = site
        template_values['rnd'] = random.randrange(1, 100)
        note = GetKindByNum('Note', 240)
        if note is False:
            note = GetKindByNum('Note', 5)
        template_values['note'] = note
        member = CheckAuth(self)
        if member:
            template_values['member'] = member
        template_values['page_title'] = site.title + u' › Plan'
        path = os.path.join(os.path.dirname(__file__), 'tpl', 'desktop', 'plan.html')
        output = template.render(path, template_values)
        self.response.out.write(output)
        
class UpdatesHandler(webapp.RequestHandler):
    def get(self):
        site = GetSite()
        template_values = {}
        template_values['site'] = site
        template_values['rnd'] = random.randrange(1, 100)
        note = GetKindByNum('Note', 240)
        if note is False:
            note = GetKindByNum('Note', 7)
        template_values['note'] = note
        member = CheckAuth(self)
        if member:
            template_values['member'] = member
        template_values['page_title'] = site.title + u' › Updates'
        path = os.path.join(os.path.dirname(__file__), 'tpl', 'desktop', 'updates.html')
        output = template.render(path, template_values)
        self.response.out.write(output)        

class AdvertiseHandler(webapp.RequestHandler):
    def get(self):
        site = GetSite()
        template_values = {}
        template_values['site'] = site
        template_values['rnd'] = random.randrange(1, 100)
        member = CheckAuth(self)
        if member:
            template_values['member'] = member
        template_values['page_title'] = site.title + u' › Advertise'
        path = os.path.join(os.path.dirname(__file__), 'tpl', 'desktop', 'advertise.html')
        output = template.render(path, template_values)
        self.response.out.write(output)

class AdvertisersHandler(webapp.RequestHandler):
    def get(self):
        site = GetSite()
        template_values = {}
        template_values['site'] = site
        template_values['rnd'] = random.randrange(1, 100)
        member = CheckAuth(self)
        if member:
            template_values['member'] = member
        template_values['page_title'] = site.title + u' › Advertisers'
        path = os.path.join(os.path.dirname(__file__), 'tpl', 'desktop', 'advertisers.html')
        output = template.render(path, template_values)
        self.response.out.write(output)
        
class InspirationHandler(webapp.RequestHandler):
    def get(self):
        site = GetSite()
        template_values = {}
        template_values['site'] = site
        template_values['rnd'] = random.randrange(1, 100)
        member = CheckAuth(self)
        if member:
            template_values['member'] = member
        template_values['page_title'] = site.title + u' › iNspiration'
        path = os.path.join(os.path.dirname(__file__), 'tpl', 'desktop', 'inspiration.html')
        output = template.render(path, template_values)
        self.response.out.write(output)
        
class DribbbleHandler(webapp.RequestHandler):
    def get(self):
        site = GetSite()
        template_values = {}
        template_values['site'] = site
        template_values['rnd'] = random.randrange(1, 100)
        member = CheckAuth(self)
        if member:
            template_values['member'] = member
        template_values['page_title'] = site.title + u' › iNspiration › dribbble'
        path = os.path.join(os.path.dirname(__file__), 'tpl', 'desktop', 'inspiration_dribbble.html')
        output = template.render(path, template_values)
        self.response.out.write(output)
        
class DribbblePopularHandler(webapp.RequestHandler):
    def get(self):
        site = GetSite()
        template_values = {}
        template_values['site'] = site
        template_values['rnd'] = random.randrange(1, 100)
        member = CheckAuth(self)
        if member:
            template_values['member'] = member
        template_values['page_title'] = site.title + u' › iNspiration › dribbble › popular'
        path = os.path.join(os.path.dirname(__file__), 'tpl', 'desktop', 'inspiration_dribbble_popular.html')
        output = template.render(path, template_values)
        self.response.out.write(output)  

class DribbbleEveryoneHandler(webapp.RequestHandler):
    def get(self):
        site = GetSite()
        template_values = {}
        template_values['site'] = site
        template_values['rnd'] = random.randrange(1, 100)
        member = CheckAuth(self)
        if member:
            template_values['member'] = member
        template_values['page_title'] = site.title + u' › iNspiration › dribbble › everyone'
        path = os.path.join(os.path.dirname(__file__), 'tpl', 'desktop', 'inspiration_dribbble_everyone.html')
        output = template.render(path, template_values)
        self.response.out.write(output)  

class DribbbleDebutsHandler(webapp.RequestHandler):
    def get(self):
        site = GetSite()
        template_values = {}
        template_values['site'] = site
        template_values['rnd'] = random.randrange(1, 100)
        member = CheckAuth(self)
        if member:
            template_values['member'] = member
        template_values['page_title'] = site.title + u' › iNspiration › dribbble › debuts'
        path = os.path.join(os.path.dirname(__file__), 'tpl', 'desktop', 'inspiration_dribbble_debuts.html')
        output = template.render(path, template_values)
        self.response.out.write(output)                                        

def main():
    application = webapp.WSGIApplication([
    ('/about', AboutHandler),
    ('/faq', FAQHandler),
    ('/plan', PlanHandler),
    ('/updates', UpdatesHandler),
    ('/advertise', AdvertiseHandler),
    ('/advertisers', AdvertisersHandler),
    ('/inspiration', InspirationHandler),
    ('/inspiration/dribbbla', DribbbleHandler),
    ('/inspiration/dribbbla/popular', DribbblePopularHandler),
    ('/inspiration/dribbbla/everyone', DribbbleEveryoneHandler),
    ('/inspiration/dribbbla/debuts', DribbbleDebutsHandler)        
    ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()