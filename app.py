from flask import Flask, request, render_template


INCHES_TO_METERS_DIVISOR = 39.97
POUNDS_TO_KILOGRAMS_DIVISOR = 2.205

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi():
    height, weight, bmi = 0, 0, 0
    if (request.method == 'POST'
        and 'height' in request.form
        and 'weight' in request.form):
        height = int(request.form.get('height')) / INCHES_TO_METERS_DIVISOR
        weight = int(request.form.get('weight')) / POUNDS_TO_KILOGRAMS_DIVISOR
        bmi = weight / (height * height)

    return render_template('index.html', bmi=bmi)

app.run()
