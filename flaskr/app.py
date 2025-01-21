from rgb_control import set_col, save_col_to_file
from flask import Blueprint, render_template, request, jsonify

app_routes = Blueprint("app_routes", __name__)

@app_routes.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        set_color(request)
    return render_template('index.html')

def set_color(request):
    data = request.get_json()

    red = data.get('red')
    green = data.get('green')
    blue = data.get('blue')
    print("Setting Values To: ", red, " ", green, " ", blue)

    set_col(red, green, blue)
    save_col_to_file(red, green, blue)

