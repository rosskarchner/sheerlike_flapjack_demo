A demonstration of using django-sheerlike with cfgov-refresh

You'll need a virtualenv with Django 1.8 and my [fork of django-sheerlike](https://github.com/rosskarchner/django-sheerlike) installed.

It expects an elasticsearch index (called 'content') to exist on localhost, populated by running 'sheer index' in cfgov-refresh.

You'll need to edit settings.py to point to a checkout of cf-gov refresh, everywhere that you see '/Users/karchner/projects/cfgov-refresh'

[This document](https://github.com/cfpb/django-sheerlike/blob/master/README.md) explains how to tweak the templates to support django-sheerlike.
