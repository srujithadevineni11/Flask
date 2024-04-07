#integrating html with flask
#http verb GET and POST
from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)
@app.route('/')
def welcome():
#we should create a seperate file called
#templates(spelling should not be changed it should be templates only) and in it we should create a index.html and write the html code 
#and save it and we can call it here using the render template.
          return render_template('index.html')

@app.route('/examresult/<int:score>')
def examresult(score):
          res=""
          if score>=50:
                    res='PASS'
          else:
                    res='FAIL'
          return render_template('results.html',result=res)

###Result checker submit html page
#the second parameter in the app.route functions
#is the methods function which can be 4 things 
#the main two are the get and post
@app.route('/submit',methods=['POST','GET'])
def submit():
          total_score=0
          if request.method=='POST':
                    Data_Science=float(request.form['datascience'])
                    Machine_Learning=float(request.form['machinelearning']) 
                    Linear_Algebra=float(request.form['linearalgebra'])
                    Statistics=float(request.form['statistics'])
                    total_score=(Data_Science+Machine_Learning+Linear_Algebra+Statistics)/4
          res=""
          return redirect(url_for('examresult',score= total_score))

if __name__=='__main__':
          app.run(debug=True)

         