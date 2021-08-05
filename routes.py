from main import app, send_from_directory, render_template


@app.route("/success", methods=["GET"])
def success():
    return render_template('success.html' )

@app.route("/blankplain", methods=["GET"])
def form_loading():
    return 'Loading...'


@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('static/assets', path)


@app.route("/", methods=["GET"])
def home():
    # ret = {"status": 1, "body": "Test"}
    return render_template('index.html')


