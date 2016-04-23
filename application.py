from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

@app.route('/application-form')
def application_form():

    return render_template('application-form.html')

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route('/application', methods=['POST'])
def application():

    positions = {'softeng': 'Software Engineer',
                'prodman': 'Product Manager',
                'qa': 'QA Engineer'}

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    salary = int(request.form.get('salreq'))
    job = request.form.get('job')

    return render_template('application-response.html', first_name=first_name,
                                                    last_name=last_name,
                                                    salary=salary,
                                                    job=positions[job])

if __name__ == "__main__":
    app.run(debug=True)
