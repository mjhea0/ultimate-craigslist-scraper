## What does this script do?

It takes a list of cities and job skills as inputs, searches computer jobs, emails you jobs (post title, link, and associated skils), and dumps the results to sqlite. Duplicate jobs are not sent or added to the database. 

## Setup

1. Clone: ` git clone git@github.com:mjhea0/ultimate-craigslist-scraper.git`
2. Navigate to the directory - `cd ultimate-craigslist-scraper`
3. Activate virtualenv:

  ```shell
  virtualenv --no-site-packages env
  source env/bin/activate
  ```

4. Setup the database: `python database.py`
5. Update your settings.py file:
  - EMAIL_USER, EMAIL_PASSWORD, TO_EMAIL, SMTP_SERVER, SMTP_PORT
  - MY_SKILLS_LIST
  - CITIES_LIST

6. Navigate to the scrapy root - `cd craigslist_jobs`
7. Run the scrapper: `scrapy crawl gigs`
8. Setup a cron to run once per week: `cron - 5 8 * * 6 /path/to/file scrapy crawl gigs`

## to do

1. Search other categories besides computer jobs
2. Option to dump to CSV
3. Proxy Servers
4. Web App
