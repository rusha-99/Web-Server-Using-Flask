#import the flask instance from entire flask package     # import render template class for render_template() inbuilt function 
from flask import Flask, render_template 

#variable __name__  to identify resources like templates, static assets and the instance folder 
#the template folder is specified as htdocs folder
#static_folder to serve static files in Flask

app = Flask(__name__,template_folder='htdocs',static_folder = 'htdocs/static')


@app.route("/") #decorator route to directed to different web pages 
def main():                                        #http://localhost:2728/ direct to main page
    return render_template('index.html')           #handle user requests and direct to .html files

@app.route("/about")
def about():                                       #http://localhost:2728/about direct to about page
    return render_template('about.html')

#to run app as localhost on port 2728
if __name__ == "__main__":
   app.run(host="localhost", port=2728, debug=True) #turn debug = True  to synchronized the application with app.py (No need to restart the application when some changes done )



