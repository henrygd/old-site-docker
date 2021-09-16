from flask import Flask, render_template, request, jsonify, \
    send_file, current_app
from functools import wraps
# import sqlite3
# import sql_stripe
import re
import sitebuilder
# import sql_sitebuilder

app = Flask(__name__)


def jsonp(func):
    """Wraps JSONified output for JSONP requests."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)
    return decorated_function


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/mailme', methods=['POST'])
def mailme():
    return 'error'


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/colorflow')
def colorflow():
    return render_template('colorflow.html')


@app.route('/makeawebsite')
def websitebuilder():
    return render_template('sitebuilder.html')


# adds contact info to database
@app.route('/sitebuildercontactinfo', methods=['POST'])
def sitebuildercontactinfo():
    if request.form['siteurl'] == "" or request.form['email'] == "":
        return jsonify(result="error1")
    else:
        email, siteurl = request.form['email'], request.form['siteurl']
        goodemail = re.compile('[\w\.]+@\w+\.[\w\.]+')
        if goodemail.match(email):
            values = (email, siteurl)
            # sql_sitebuilder.addvalues(values)
            return jsonify(result="success")
        else:
            return jsonify(result="error2")


@app.route('/stripeserver')
def stripeserver():
    return render_template('stripeserver.html')


# adds keys to database
@app.route('/addkey', methods=['POST'])
def addkey():
    goodpub = re.compile("^pk_(test|live)_[a-zA-Z0-9]{24}$")
    goodsec = re.compile("^sk_(test|live)_[a-zA-Z0-9]{24}$")
    goodemail = re.compile('[\w\.]+@\w+\.[\w\.]+')
    public, secret = request.form['publishablekey'], request.form['secretkey']
    email = request.form['email']
    if goodpub.match(public) and goodsec.match(secret) and goodemail.match(email):
        return jsonify(result="error1")
    else:
        return jsonify(result="error2")


# takes publishable/public key, returns matched secret key from db
@app.route('/getkey')
def getkey():
    if re.compile("^pk_(test|live)_[a-zA-Z0-9]{24}$").match(request.args.get('a')):
        return jsonify(result="error1")
    else:
        return jsonify(result="error2")


# takes stripe token, other parameters, creates stripe charge
@app.route('/charge')
@jsonp
def stripecharge():
    return jsonify(error={'message': 'Service no longer available. Apoligies!'})


@app.route('/testsite', methods=['POST'])
def convert():
    content = sitebuilder.build(
        styles=request.form['style'],
        logo=request.form['logo'],
        background=request.form['background'],
        orgfont=request.form['orgfont']+'\n\t',
        showfont=request.form['showfont']+'\n\t',
        bodyfont=request.form['bodyfont']+'\n\t',
        butthov=request.form['butthov'],
        logocolor=request.form['logocolor'],
        barcolor=request.form['barcolor'],
        buttoncolor=request.form['buttoncolor'],
        navbartext=request.form['navbartext'],
        introtextcolor=request.form['introtextcolor'],
        aboutback=request.form['aboutback'],
        eventsback=request.form['eventsback'],
        contactback=request.form['contactback'],
        contacticons=request.form['contacticons'],
        linkcolor=request.form['linkcolor'],
        mapcoords=request.form['mapcoords'],
        twitter=request.form['twitter'],
        facebook=request.form['facebook'],
        youtube=request.form['youtube'],
        orgname=request.form['orgname'],
        navabout=request.form['navabout'],
        navevents=request.form['navevents'],
        navcontact=request.form['navcontact'],
        introtext=request.form['introtext'],
        abouthead=request.form['abouthead'],
        aboutsub=request.form['aboutsub'],
        aboutcont=request.form['aboutcont'],
        eventhead=request.form['eventhead'],
        contacthead=request.form['contacthead'],
        phone=request.form['phone'],
        address=request.form['address'],
        email=request.form['email'],
        mandrill_api=request.form['mandrill_api'],
        stripepk=request.form['stripepk'],
        cal_id=request.form['cal_id'],
        cal_api=request.form['cal_api'],
        eventstatus=request.form['eventstatus'],
        mapstatus=request.form['mapstatus']
        )
    if request.form['downloadstatus'] == "testbtn":
        with open('templates/test.html', 'w') as thefile:
            thefile.write(content)
        return jsonify(url='/preview', modal="#PreviewModal")
    else:
        with open('static/index.html', 'w') as thefile:
            thefile.write(content)
        return jsonify(url='/downloadsite', modal="#byeModal")


@app.route('/preview')
def preview():
    return render_template('test.html')


@app.route('/downloadsite')
def downloadsite():
    return send_file('static/index.html', as_attachment=True)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0")
