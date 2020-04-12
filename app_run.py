import json

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import url_for

import models.person
import models.text
import models.page_ids
import models.japanese_text
from utils import cipher
from utils import util

app = Flask(__name__, template_folder='./templates', static_folder='./static')


# UI
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        op = models.page_ids.UserOperation()
        all_data = op.read_database()
        username = session['username']
        return render_template('./home.html', all_data=all_data, for_all_data=range(len(all_data)), username=username)
    return redirect('/login')

@app.route('/<int:pk>', methods=['GET', 'POST'])
def page_id(pk):
    if 'username' in session:
        op = models.page_ids.UserOperation()
        try :
            op.id_title(pk)
            user_agent = request.headers.get('user-agent')
            if 'Mobile' in user_agent:
                user_agent = 'mobile'
            else:
                user_agent = 'pc'
            username = session['username']
            return render_template('./chat.html' , pk=pk, username=username, user_agent=user_agent)
        except:
            return redirect(url_for('index', nothing_page='this page is not existence'))
    return redirect('/login')

@app.route('/make_page', methods=['GET', 'POST'])
def make_page():
    if 'username' in session:
        if request.method == 'POST':
            op = models.page_ids.UserOperation()
            page_name_title = request.form['page_name_title']
            op.create_page(page_name_title)
            page_id = op.key_title(page_name_title)
            return redirect(f'/{page_id}')
        username = session['username']
        return render_template('./make_page.html' , username=username)
    return redirect('/login')

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mail_address = request.form['mail_address']
        address = request.form['address']

        op = models.person.UserOperation()
        op.create_user(username, password, mail_address, address)

        print(op.read_database())

        return redirect('/login')
    return render_template('./signup.html')

@app.route('/login', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        op = models.person.UserOperation()
        request_username = request.form['username']
        request_password = request.form['password']
        if op.check_user(request_username, request_password):
            session['username'] = request_username
        else:
            fail = 'I am not able to log in to the site. Can you please look into it for me?'
            return render_template('./login.html', fail=fail)
        return redirect('/')

    if 'username' in session:
        return redirect(url_for(index))
    return render_template('./login.html')
# end UI

@app.route('/logout', methods=['GET'])
def log_out():
    session.pop('username', None)
    return redirect('/login')

# database write
@app.route('/model', methods=['GET', 'POST'])
def model():
    if request.method == 'POST':
        # file_op = models.text.UserOperation()
        # encode = cipher.ShiftCipher()
        # letter = encode.shift_letters_encode(request_json['text'], 3)
        request_json = request.json
        username = session['username']
        letter = request_json['text']
        page_id = request_json['page_id']
        japanese_letters = request_json['to_japanese_letters']

        if util.alphabet_check(letter):
            print(request_json, username, letter, page_id, japanese_letters)
        else:
            print(request_json, username, letter, page_id)
        # file_op.create_text(username, letter, page_id)
        try:
            request_json = json.dumps(request_json)
            return request_json, 200
        except:
            return render_template('400 errer'), 400

# render json
@app.route('/text.json/<int:pk>')
def text(pk):
    file_op = models.text.UserOperation()
    f = file_op.read_page_id(pk)

    return jsonify(f), 200

# session secret key
app.secret_key = 'gasgsabshsdhersdgdgsd'


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8085,
                        type=int, help='port listen on')
    args = parser.parse_args()
    port = args.port


    app.run(host='localhost', port=port, threaded=True, debug=True)