# "Database code" for the DB news.

import datetime
import psycopg2
import bleach

POSTS = [("This is the first post, that comes by default.", datetime.datetime.now())]

DBNAME = "news"

def get_posts(q):
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  conn = db.cursor()
  co = '/articles/'
  if q == "Q1":
      conn.execute("select articles.title, count(*) as num from articles, log where log.path like '%' || articles.slug || '%' group by articles.title order by num desc;")

  if q == "Q2":
          conn.execute("select authors.name, count(*) as num from authors, articles, log where authors.id = articles.author and log.path like '%' || articles.slug || '%' group by authors.name order by num desc;")

  if q == "Q3":
        conn.execute("select time::date, (count(status != '200 OK')*100/(select count(*) from log)::float) as num from log group by time::date;")

  return conn.fetchall()
  db.close()
