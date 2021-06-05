from flask import Flask, app, render_template, redirect,request

app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if(request.method=='POST'):
        url=request.form.get('url')
        return(render_template('index.html',))
    return(render_template('index.html'))
@app.route('/<id>',methods=['GET'])
def revoke(id):
    return("<h1>Success</h1>")
    
app.run(debug=True)