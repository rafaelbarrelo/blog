#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'rafaelbarrelo'
SITENAME = u'rafaelbarrelo.blog'
SITEURL = u''

PATH = 'content'
THEME = 'pelican-simplegrey'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/rafaelbarrelo'),
          ('GitHub', 'https://github.com/rafaelbarrelo'),)

DEFAULT_PAGINATION = 30

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
