import alchemy

AUTHOR = 'Mark Snidal'
SITENAME = "msnidal"
SITEURL = 'https://msnidal.com'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("GitHub", "https://github.com/msnidal"),("Twitter", "https://twitter.com/marksnidal"))
SOCIAL = ()

DEFAULT_PAGINATION = 10

THEME = 'themes/pelican-alchemy/alchemy'

STATIC_PATHS = ["static"]
EXTRA_PATH_METADATA = {
    "static/favicon.ico": {"path": "favicon.ico"},
}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True