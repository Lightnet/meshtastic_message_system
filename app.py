import meshtastic
import meshtastic.serial_interface
import sqlite3
import jwt
import flask
from flask import g, Flask, render_template, send_from_directory, jsonify, request
# https://stackoverflow.com/questions/59355194/python-flask-error-failed-to-load-module-script-strict-mime-type-checking-i
# https://github.com/pallets/flask/issues/1045
# https://github.com/encode/starlette/issues/829
# https://stackoverflow.com/questions/56587108/flask-how-to-use-es6-modules
import mimetypes
#from mimetypes import guess_type
mimetypes.init()
# print(mimetypes.knownfiles)
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('application/javascript', '.mjs')
mimetypes.add_type('text/css', '.css')

#print("init...")
#con = sqlite3.connect("sqlite3.db")

user_table = """CREATE TABLE if NOT EXISTS user(
  id integer PRIMARY KEY,
  alias,
  passphrase,
  role TEXT,
  at_created datetime DEFAULT CURRENT_TIMESTAMP,
  at_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

# def initDB():
#   cur = con.cursor()
#   #cur.execute("CREATE TABLE if NOT EXISTS movie(title, year, score)")
#   cur.execute(user_table)
#   res = cur.execute("SELECT name FROM sqlite_master")
#   print(res.fetchone())
#initDB()

# https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty-in-python
def is_not_blank(s):
  return bool(s and not s.isspace())

DATABASE = 'sqlite3.db'
SECRET = 'SECRET'

# setup database for flask
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
#app init
app = Flask(
  __name__,
  static_url_path='/'
)

@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g, '_database', None)
  if db is not None:
    db.close()

@app.route("/")
def indexPage():
  #return "<p>Hello, World!</p>"
  #jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
  token = request.cookies.get('token')
  if token:
    print("token ENC: ", token)
    token = jwt.decode(token, "secret", algorithms=["HS256"])
    print("token parse: ", token)
  return render_template("index.html")

@app.route('/api/auth/signin', methods=['POST'])
def auth_signin():
  content_type = request.headers.get('Content-Type')
  print("content_type: ", content_type)
  if content_type == 'application/json':
    cur = get_db().cursor()
    data = request.json
    print("data: ", data)
    if is_not_blank(data.get("alias")):
      alias = data.get("alias")
      passphrase = data.get("passphrase")
      cur.execute("SELECT * FROM user WHERE alias = ?", (alias,))
      result = cur.fetchone()
      if result is None:
        return jsonify({"api":"DONOTEXIST"})
      else:
        print("fetchone: ", result)
        #print("alias: ", result.alias)#nope
        print("alias: ", result[1])
        if result[1] == alias and result[2] == passphrase:
          encoded_jwt = jwt.encode({"alias": result[1], "role":"member"}, "secret", algorithm="HS256")
          #need json here
          resp  = flask.make_response(jsonify({"api":"PASS"}))
          #set cookie
          resp.set_cookie("token", value=encoded_jwt)
          #return jsonify({"api":"PASS"})  
          return resp
        return jsonify({"api":"FAIL"})
    #uuid="test"
    #return jsonify({"uuid":uuid})
    return jsonify({"api":"FAIL"})
  else:
    return "Content type is not supported."
# https://stackoverflow.com/questions/59817019/checking-if-a-username-exists-within-a-sqlite-database
@app.route('/api/auth/signup', methods=['POST'])
def auth_signup():
  content_type = request.headers.get('Content-Type')
  print("content_type: ", content_type)
  if content_type == 'application/json':
    data = request.json
    #print("data: ", data)
    #print("alias: ", data.get("alias"))
    if data.get("alias"):
      cur = get_db().cursor()
      alias = data.get("alias")
      passphrase = data.get("passphrase")
      print("alias: ", alias)
      #res = cur.execute(f'SELECT alias FROM user WHERE alias MATCH {alias}') # not recommend for inject sql
      cur.execute("SELECT * FROM user WHERE alias = ?", (alias,))
      #get_db().commit()
      #print("res: ",res)
      #print("rowcount: ",res.rowcount)
      if cur.fetchone() is None:
        cur.execute("INSERT INTO user (alias, passphrase ) VALUES (?, ?);", (alias,passphrase))
        get_db().commit()
        return jsonify({"api":"CREATED"})
      else:
        return jsonify({"api":"EXIST"})
    #uuid="test"
    #return jsonify({"uuid":uuid})
    return "Content type is not supported."
  else:
    return "Content type is not supported."

@app.route('/components/<path:filename>')
def static_components(filename):
  #myfile = '/components/'+filename
  #print("myfile: ", myfile)
  return send_from_directory('static', 'components/'+filename)

@app.route('/index.js')
def static_index_js():
  return send_from_directory('static', 'index.js')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/user/<username>') 
# def show_user(username): 
#     # Greet the user 
#     return f'Hello {username} !' 

# Pass the required route to the decorator. 
# @app.route("/hello") 
# def hello(): 
#     return "Hello, Welcome to GeeksForGeeks"

if __name__ == '__main__':
  #print(app.config)
  #app.run()
  app.run(debug = True)
  print("http://127.0.0.1:5000")
  pass