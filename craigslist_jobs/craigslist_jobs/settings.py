import os

BOT_NAME = 'craigslist_jobs'

SPIDER_MODULES = ['craigslist_jobs.spiders']
NEWSPIDER_MODULE = 'craigslist_jobs.spiders'
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 AlexaToolbar/alxg-3.1"
#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:8.0.1) Gecko/20100101 Firefox/8.0.1'

ITEM_PIPELINES = ['craigslist_jobs.pipelines.GigPipeline']

TO_EMAIL = ''
EMAIL_USER = ''
EMAIL_PASSWORD = ''
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = '587' 

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DATABASE_NAME = os.path.join(PROJECT_ROOT, 'db_gigs.db')

CITIES_LIST = ['sfbay', 'newyork', 'boston', 'denver', 'austin', 'la']
MY_SKILLS_LIST = ['python', 'ruby']

try:
    from settings_local import *
except ImportError:
    pass