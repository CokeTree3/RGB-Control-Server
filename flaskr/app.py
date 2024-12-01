from rgb_control import set_col
from flask import Blueprint, render_template, request

app_routes = Blueprint("app_routes", __name__)

@app_routes.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

@app_routes.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        set_color(request)
    return render_template('index.html')

def set_color(request):
    red = int(request.form['red'])
    green = int(request.form['green'])
    blue = int(request.form['blue'])

    set_col(red, green, blue)

