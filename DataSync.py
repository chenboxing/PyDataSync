import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import sys
import os

app = Flask(__name__)


# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE='D:\Projects\DataSync\datasync.sqlite3',
    #DATABASE='datasync.sqlite3',
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


#DB related functions
def connect_db():
    """Returns a new connection to the sqlite database"""
    return sqlite3.connect(app.config['DATABASE'], detect_types=sqlite3.PARSE_DECLTYPES)

def init_db():
    """Create the database if it doesn't exist"""
    if not os.path.isfile(app.config['DATABASE']):
        app.logger.debug('DB disappeared, making a new one')
        db = connect_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def query_db(query, args=(), one = False):
    """Query database returning dictionary"""
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
        for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

@app.before_request
def before_request():
    init_db()
    g.db = connect_db()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():

"""
 db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
 db.commit()

  cur = db.execute('select title, text from entries order by id desc')
entries = cur.fetchall()


  g.db.cursor().execute('INSERT INTO entries VALUES (?, ?, ?, ?, ?, ?, ?)',
                (None,
                entry['link'],
                "http://www.sharms.org/static/twitter_1.png",
                entry['summary'],
                "twitter",
                datetime.strptime(entry['updated'][:-6], '%a, %d %b %Y %H:%M:%S'),
                datetime.now()))

    g.db.commit()

"""


    sources = query_db('select * from sources')
    #return 'Hello World! %s ' % sources[0]['name']
    return render_template('index.html', sources = sources)

if __name__ == '__main__':
    app.run()
