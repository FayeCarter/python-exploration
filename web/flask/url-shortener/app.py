from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'g7892o3irnewdfhs89djshgk'

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
  if request.method == 'POST':
    urls = {}
    if os.path.exists('urls.json'):
      with open('urls.json') as urls_file:
        urls = json.load(urls_file)

    if request.form['code'] in urls.keys():
      flash('That short name has already been taken. Please select a new name')
      return redirect(url_for('home'))

    if 'url' in request.form.keys():
      urls[request.form['code']] = {'url': request.form['url']}
    else:
      new_file = request.files['file']
      full_name = request.form['code'] + secure_filename(new_file.filename)
      new_file.save('/Users/FayeCarter/Documents/Projects/python/web/flask/url-shortener/' + full_name)
      urls[request.form['code']] = {'file': full_name}

    with open('urls.json', 'w') as url_file:
      json.dump(urls, url_file)
    return render_template('your_url.html', code=request.form['code'])
  else:
    return redirect(url_for('home'))

@app.route('/<string:code>')
def redirect_to_url(code):
  if os.path.exists('urls.json'):
    with open('urls.json') as urls_file:
      urls = json.load(urls_file)
      if code in urls.keys():
        if 'url' in urls[code].keys():
          return redirect(urls[code]['url'])