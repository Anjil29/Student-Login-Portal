from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def home():
    return "Flask is working"

@app.route('/login',methods=['POST'])
def login():
    name=request.form['name']
    roll_no=request.form['rollno']
    password=request.form['password']
    
    if(name=="" or roll_no=="" or password==""):
        return render_template(
            'error.html',
            message="No field empty"
        )
    if(len(password)<6):
        return render_template(
            'error.html',
            message="Password minimum 6 characters"
        ) 
    if(not roll_no.isdigit()):
        return render_template(
            'error.html',
            message="Roll number must contain only numbers"
        )   
        
    if(roll_no=="101" and password=="student123"):
        return render_template(
            'success.html',
            name=name,
            rollno=roll_no
        )
    else:
        return render_template(
            'error.html',
            message="Error"
        )    
              
if(__name__=='__main__'):
    app.run(debug=True)