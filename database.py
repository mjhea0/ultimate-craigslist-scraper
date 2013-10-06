import sqlite3
 
conn = sqlite3.connect("craigslist_jobs/craigslist_jobs/db_gigs.db")
 
cursor = conn.cursor()
 
# create a table
cursor.execute("""CREATE TABLE gigs(name text, url text, skills text, gig_datetime datetime, sent boolean) """)


conn.commit()



