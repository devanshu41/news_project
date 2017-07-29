# "Database code" for the DB Forum. Media obessed with bear

import datetime
import psycopg2
import bleach

POSTS = [("This is the first post, that comes by default.", datetime.datetime.now())]

DBNAME = "news"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  conn = db.cursor()
  #conn.execute("select id, status from log where status != '200 OK' limit 10;")
  #conn.execute("select author, slug from articles;") LIKE '%'  || account_invoice.origin || '%'
  co = '/articles/'
  # Solutio 1 ------ conn.execute("select articles.title, count(*) as num from articles, log where log.path like '%' || articles.slug || '%' group by articles.title order by num desc;")
  # Solutio 2 ------ conn.execute("select authors.name, count(*) as num from authors, articles, log where authors.id = articles.author and log.path like '%' || articles.slug || '%' group by authors.name order by num desc;")
  conn.execute("select time::date, (count(status != '200 OK')*100/(select count(*) from log)::float) as num from log group by time::date;")
  return conn.fetchall()
  db.close()

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  clean_content = bleach.clean(content)
  POSTS.append((clean_content, datetime.datetime.now()))
  db = psycopg2.connect(database=DBNAME)
  conn = db.cursor()
  conn.execute("insert into posts (content) values(%s)", (clean_content,))
  #conn.execute("insert into posts (content) values('%s')" % clean_content) This avoids the breaking of the string ref:----web comic xkcd
  db.commit()
  db.close()
