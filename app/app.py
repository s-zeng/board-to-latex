from flask import Flask, request, jsonify
import sqlite3
import bcrypt
import secrets
import time
import schedule
import uuid
import json
import ocr_gcp
import os

app = Flask(__name__)
valid_tokens = {}


def init():
    db = get_db()
    db.execute('CREATE TABLE IF NOT EXISTS users ('
                     'username VARCHAR,'
                     'password VARCHAR,'
                     'uuid VARCHAR)')
    db.commit()
    schedule.every(5).minutes.do(invalidate_inactive_tokens)


@app.route("/")
def root():
    return "ya YEET"


@app.route("/api/login", methods=['POST'])
def login():
    if not request.form['username'] or not request.form['password']:
        return jsonify({'error': 'Missing form params username or password'})

    username = request.form['username']
    provided_pass = request.form['password']

    result = get_db().execute('SELECT password FROM users WHERE username=(?)', (username,)).fetchall()

    if len(result) > 0:
        hash_pass = result[0][0]
    else:
        return jsonify({'error': 'Invalid credentials.'})

    if check_password(str(provided_pass).encode(), hash_pass.encode()):
        token = secrets.token_hex(20)
        user_uuid = get_uuid(username)
        valid_tokens[token] = {'uuid': user_uuid, 'expiry': int(round(time.time() * 1000)) + 300000}
        return jsonify({'token': token, 'uuid': user_uuid})
    else:
        return jsonify({'error': 'Invalid credentials.'})


@app.route("/api/register", methods=['POST'])
def register():
    if not request.form['username'] or not request.form['password']:
        return jsonify({'error': 'Missing form params username or password.'})

    username = request.form['username']
    provided_pass = request.form['password']
    if user_exists(username):
        return jsonify({'error': 'Username already taken.'})

    db = get_db()
    register_vars = (username, get_hashed_password(str(provided_pass).encode()).decode("utf-8"), str(uuid.uuid4()))
    db.execute('INSERT INTO users(username, password, uuid) VALUES (?, ?, ?)', register_vars)
    db.commit()

    return jsonify({'success': 'User registered.'})


@app.route("/api/images", methods=['GET', 'POST'])
def images():
    if request.method == 'GET':
        if request.args.get('token'):
            token = request.args.get('token')
            if is_token_valid(token):
                update_token(token)
                photos = []
                user_uuid = valid_tokens[token]['uuid']
                for file in os.listdir('photos'):
                    if file.startswith(user_uuid) and not file.endswith('.tex'):
                        photos.append(os.path.join(os.path.abspath(''), 'photos', file))
                return jsonify({'paths': photos})

            else:
                return jsonify({'error': 'Invalid token.'})
        else:
            return jsonify({'error': 'Missing form params token.'})

    elif request.method == 'POST':
        if request.form['token'] and request.form['file']:
            token = request.form['token']
            if is_token_valid(token):

                path = str(request.form['file'])
                new_path = path[:path.rfind('.')] + '.tex'

                # If tex is already rendered or not
                if not os.path.exists(new_path):
                    rendered = ocr_gcp.get_text(request.form['file'])
                else:
                    return jsonify({'path': new_path})

                # Render tex
                if rendered is not None:

                    with open(new_path, 'w+') as ocr_save:
                        ocr_save.write(json.dumps(rendered))

                    # Return path to tex file
                    return jsonify({'path': new_path})

                else:
                    return jsonify({'error': 'File not found.'})
            else:
                return jsonify({'error': 'Invalid token.'})
        else:
            return jsonify({'error': 'Missing form params token or file.'})


# Checks if a username exists in the db
def user_exists(username):
    user = get_db().execute('SELECT username FROM users WHERE username=(?)', (username,)).fetchall()
    if len(user) > 0:
        return True
    return False


def get_uuid(username):
    uuid_user = get_db().execute('SELECT uuid FROM users WHERE username=(?)', (username,)).fetchall()
    if len(uuid_user) > 0:
        return uuid_user[0][0]
    return None


# Gets a uuid from a token
def get_uuid_from_token(token):
    if is_token_valid(token):
        return valid_tokens[token]['uuid']
    return None


# Invalidates all inactive tokens (5 minute inactivity)
def invalidate_inactive_tokens():
    curr_time = int(round(time.time() * 1000))
    for token, info in valid_tokens.items():
        if info['expiry'] > curr_time:
            valid_tokens[token] = None


# Updates a token to keep it alive
def update_token(token):
    if is_token_valid(token):
        # Add 5 minutes
        valid_tokens[token]['expiry'] = int(round(time.time() * 1000)) + 300000


# Checks if a token is valid (exists)
def is_token_valid(token):
    if valid_tokens.get(token):
        return True
    return False


def get_db():
    return sqlite3.connect('data.db')


def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())


def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password)


if __name__ == '__main__':
    init()
    app.run(debug=True)
