# "Database code" for the DB news.

import datetime
import psycopg2

POSTS = [("This is the first post, that comes by default.", datetime.datetime.now())]

DBNAME = "news"

def get_posts(q):
  """Returns the soution queries in the sequence asked."""
  db = psycopg2.connect(database=DBNAME)
  conn = db.cursor()
  co = '/articles/'
  if q == "Q1":
      conn.execute("select articles.title, count(log.path) as num from articles, log where log.path like '%' || articles.slug || '%' and log.status = '200 OK' group by articles.title order by num desc;")

  if q == "Q2":
          conn.execute("select authors.name, count(log.path) as num from authors, articles, log where authors.id = articles.author and log.path like '%' || articles.slug || '%' and log.status = '200 OK' group by authors.name order by num desc;")

  if q == "Q3":
        conn.execute("select time::date, (count(status != '200 OK')*100/(select count(*) from log)::float) as num from log group by time::date;")
        #, (count(status != '200 OK')*100/(select count(*) from log)::float) as num
        #select a.time::date, (count(a.status != '200 OK')*100/(count (b.status))::float) as num from log a, log b where a.time::date = b.time::date group by a.time::date;")

  return conn.fetchall()
  db.close()
