from flask import Flask,render_template,send_from_directory
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
  static_folder = os.path.join(app.route_path, 'static')
  png_files = [f for f in os.listdir(static_folder) if f.endswith('.png')]

  random_png = random.choice(png_files)

  return render_template('index.html', random_png=random_png)

@app.route('/static/<path:path>')
def serve_static(path):
  return send_from_directory('static', path)

if __name__ = '__main__':
	app.run()
