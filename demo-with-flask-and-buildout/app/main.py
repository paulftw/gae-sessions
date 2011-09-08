import sys
sys.path.insert(0, './libs')
sys.path.insert(0, './libs.zip')


from flask import Flask, render_template, request, session
import datetime, os
from gaesessions import SessionMiddleware, get_current_session

# Create a Flask app
app = Flask(__name__)

# Inject gae-sessions into the app
app.wsgi_app = SessionMiddleware(app.wsgi_app, cookie_key=os.urandom(64),
                                 lifetime=datetime.timedelta(days=7))

@app.route("/")
def index():
    session = get_current_session()
    if session.has_key('counter'):
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html', counter = session['counter'])


"""
App Engine entry point.
"""

def main():
    from google.appengine.ext.webapp.util import run_wsgi_app
    run_wsgi_app(app)


# Use App Engine app caching
if __name__ == "__main__":
    main()
