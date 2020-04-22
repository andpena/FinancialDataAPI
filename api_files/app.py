import os
from flask import Flask, send_from_directory, render_template
from blueprints import restapi, webui

app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"),"favicon.ico", mimetype="image/vnd.microsoft.icon")


restapi.init_app(app)
webui.init_app(app)