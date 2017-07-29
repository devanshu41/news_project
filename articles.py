#!/usr/bin/env python3
#

from flask import Flask, request, redirect, url_for

from articlesdb import get_posts

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB Forum</title>
    <style>
      h1, h2, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>DB newsdata</h1>
    <!-- post content will go here -->
%s
  </body>
</html>
'''

# HTML template for Query 1
POST1 = '''\
    <div class=post><em class=date>%s</em><br>%s</div>
'''

# HTML template for Query 2
POST2 = '''\
    <div class=post><em class=date>%s</em><br>%s</div>
'''

# HTML template for Query 3
POST3 = '''\
    <div class=post><em class=date>%s %%</em><br>%s</div>
'''

@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  posts1 = "".join(POST1 % (integer, text) for text, integer in get_posts("Q1"))
  posts2 = "".join(POST2 % (integer, text) for text, integer in get_posts("Q2"))
  posts3 = "".join(POST3 % (integer, text) for text, integer in get_posts("Q3"))
  posts = "<h2>What are the most popular three articles of all time?</h2>" + posts1 + "<h2>Who are the most popular article authors of all time?</h2>" + posts2 + "<h2>On which days did more than 1% of requests lead to errors?</h2>" + posts3
  html = HTML_WRAP % posts
  return html

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
