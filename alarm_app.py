from flask import Flask, render_template, request, redirect, url_for, abort
import os
import time
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'sound_clips'
app.config['UPLOAD_EXTENSIONS'] = '.mp3'

#The default home page
@app.route('/', methods = ['POST', 'GET'])
def home():
	return 'Home Page!'

#The page that displays after a successful upload before redirecting back to the upload page
@app.route('/Success', methods = ['POST', 'GET'])
def success():
	render_template('Success_pg.html')
	time.sleep(5)
	return redirect(url_for('upload'))

#Thwe upload page that lists the files in rotation and lets you upload more files
@app.route('/uploads', methods = ['POST', 'GET'])
def upload():
	path = '/home/ubuntu/alarm_project/sound_clips'
	files = os.listdir(path)
	if request.method == 'POST':
		f = request.files['file']
		filename = secure_filename(f.filename)
		file_ext = os.path.splitext(filename)[1]
		if file_ext not in app.config['UPLOAD_EXTENSIONS']:
			abort(400)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return redirect(url_for('success'))
	return render_template('uploads_pg.html', data=files)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
