from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/results')
def show_results():
    message_dict = request.args
    message_list = [value for key, value 
                    in message_dict.items(multi=True) 
                    if key == 'message']

    session['message'] = message_list
    return render_template('results.html')

@app.route('/save_name', methods=['POST'])
def save_name():
    input_name = request.form.get("name")
    session['name'] = input_name
    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
