"""
GAE-Sessions
-----------

Fast, lightweight Sessions middleware for Google App Engine
(memcache + datastore)

Links
`````

* `documentation <http://wiki.github.com/dound/gae-sessions/>`_
* `development version
  <http://github.com/dound/gae-sessions/zipball/master#egg=GAE-Sessions-dev>`_
"""
from setuptools import setup


setup(
    name='GAE-Sessions',
    version='1.07',
    url='http://github.com/dound/gae-sessions',
    license='Apache License 2.0',
    author='David Underhill',
    author_email='DAVID, WHAT"S YOUR EMAIL??? ***',
    description='Sessions middleware for Google App Engine',
    packages=['gaesessions'],
    namespace_packages=['gaesessions'],
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)