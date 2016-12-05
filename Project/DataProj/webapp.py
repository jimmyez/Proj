from flask import Flask, request, render_template
app = Flask(__name__)  

@app.route("/")
def root():
    return app.send_static_file('index.html')

	
@app.route("/index")
def index(name=None): 
     return render_template('index.html', name=name)
	
	
@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact") 
@app.route('/contact')
def contact():         
	return render_template('contact.html')

	
	
if __name__ == "__main__":     
	app.run()
