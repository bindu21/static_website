from flask import Flask

app=Flask(__name__)

@app.route('/')
def my_fun():
	return "I am Home page"
	
@app.route('/about/')
def new_fun():
	return "I am now about page"
	
if __name__ == "__main__":
	app.run(debug=True)