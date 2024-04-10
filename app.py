import meshtastic
import meshtastic.serial_interface

from flask import Flask, render_template, send_from_directory
# https://stackoverflow.com/questions/59355194/python-flask-error-failed-to-load-module-script-strict-mime-type-checking-i
# https://github.com/pallets/flask/issues/1045
# https://github.com/encode/starlette/issues/829
# https://stackoverflow.com/questions/56587108/flask-how-to-use-es6-modules
import mimetypes
from mimetypes import guess_type
mimetypes.init()
# print(mimetypes.knownfiles)
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('application/javascript', '.mjs')
mimetypes.add_type('text/css', '.css')

#print("init...")

app = Flask(
  __name__,
  static_url_path='/'
)

@app.route("/")
def indexPage():
  # mimetypes.add_type('application/javascript', '.js')
  # mimetypes.add_type('text/css', '.css')
  # mimetypes.add_type('image/svg+xml', '.svg')
  #return "<p>Hello, World!</p>"
  return render_template("index.html")

@app.route('/components/<path:filename>')
def static_components(filename):
  myfile = '/components/'+filename
  print("myfile: ", myfile)
  return send_from_directory('static', 'components/'+filename)
#     return send_from_directory(app.config['ES6_MODULES'],
#                                filename, as_attachment=True,
#                                mimetype='text/javascript'
#     )

@app.route('/index.js')
def static_index_js():
  return send_from_directory('static', 'index.js')
    # return send_from_directory(
    #   directory=app.config['APPLICATION_ROOT'],
    #   filename='/static/index.js',
    #   as_attachment=True,
    #   mimetype='text/javascript'
    # )

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
  print(app.config)
  #app.run()
  #print(mimetypes)
  #mimetypes.init()
  #print(mimetypes.knownfiles)
  # mimetypes.add_type('application/javascript', '.js')
  # mimetypes.add_type('text/css', '.css')
  #print(mimetypes.knownfiles)
  #print(guess_type("something.js",strict=False))
  print(guess_type("something.js"))
  # print(guess_type("something.css"))
  # print(guess_type("something.svg"))
  app.run(debug = True)
  print("http://127.0.0.1:5000")
  pass