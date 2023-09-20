from flask import Flask, jsonify, request, render_template, session, redirect, url_for


app = Flask(__name__ , static_folder = 'statics', static_url_path ='/statics')
app.add_url_rule('/statics/<path:filename>', endpoint='statics', view_func=app.send_static_file)

# Set a random string for the secret key of session
app.secret_key = "the secret key"


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5500)
