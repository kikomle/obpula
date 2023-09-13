from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/submit_login_info', methods=['POST'])
def receive_login_info():
    name = request.form['name']
    return redirect(url_for('show_thanks', name=name))

@app.route('/thanks/<name>')
def show_thanks(name):
    print(name)
    return render_template('thanks.html', name = name)

@app.route('/quest/<quest_id>') # <quest_id> is the number of the quest
def quest(quest_id):
    return render_template(f'/quests/quest.html', quest_question = "Is 2023 even?", quest_id = quest_id)

# get the response from the user from quest.html
@app.route('/submit_quest_response/<quest_id>', methods=['POST'])
def submit_quest_response(quest_id):
    response = request.form['response']
    return redirect(url_for('show_quest_response', quest_id=quest_id, response=response))

if __name__ == '__main__':
    app.run(debug=True)