from flask import Flask, render_template, request ,redirect

app = Flask(__name__)

message_list = []
user_list = []


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template("board.html", message_list=message_list)
    if request.method == 'POST':
        username = request.form['username']
        user_count = user_list.count(username) +1
        user_list.append(username)
        message = request.form['message']
        if username == '':
            message_list.append(f'名無しさん:{message}')
            return redirect("/")
        message_list.append(f'{username} [{user_count}]: {message}')
        return redirect("/")


if __name__ == '__main__':
    app.run(debug=True, port=8888)
