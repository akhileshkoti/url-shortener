from models import create_hash
from flask import Flask, app, render_template, redirect,request
from models import create_hash,revoke

app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if(request.method=='POST'):
        url=request.form.get('url')
        hash=create_hash(url)
        return(render_template('shorten.html',url=hash))
    return(render_template('index.html'))
@app.route('/<id>',methods=['GET'])
def open(id):
    print(id)
    url=revoke(id)
    if(url != "create new"):
        return(redirect(url))
    return(redirect('/'))    
app.run(debug=True)