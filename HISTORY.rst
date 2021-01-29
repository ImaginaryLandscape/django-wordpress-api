.. :changelog:

History
-------

0.2.1 (2021-01-29)
++++++++++++++++++

* Dropped support for python <3.6, Django <2.0
* Updated iso8601, requests, wheel dependencies
* Changed responses dependency to load from pypi
* Fix documentation to mention support for WP API v2
* Corrected Bumpversion config, changed to Bump2Version
* Tested against Python 3.6 and Django 2.2

Untagged Release (2020-07-19)
+++++++++++++++++++++++++++++

* Update urls.py
  Add str methods on cms plugin models
  Loading cms choices in form classes to avoid the need for migrations
  Fixed cache name for latest blog tag
  Removed plugin template labels
  Added basic cms plugins for listing latest events and events by author, category, or tag
  Added template tags to fetch blog posts by category and tag
  Added caching to blogs by author template tag
  Changed 404 to simple return so the authors template tag fails silently
  Upped API connector timeouts from 30 to 60s
  Updated tag filter key to work with API v2
  Fixed related blog tag context
  Upped six requirement
  Added additional contexts in author template tag
  Added tag list to related blob objects
  Update wp_api_tags.py
  Create wp_api_tags.py
  Added __init__.py to templatetags dir
  Update utils.py
  Added page range to context

* Added start and end index to list views, added tags and categories to list
  posts, fixed non-working cached search, fixed detail views by changing the
  filter key

0.2.0 (2019-03-04)
++++++++++++++++++

* last upstream release

0.1.0 (2016-09-02)
++++++++++++++++++

* First release on PyPI.
