from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class WordFilter:
    def __init__(self, NG_word_list, replace_word):
        self.NG_word_list = NG_word_list
        self.replace_word = replace_word

    def censor(self, sentence):
        replace_sentence = sentence
        for NG_word in self.NG_word_list:
            replace_sentence = replace_sentence.replace(NG_word, self.replace_word)
        return replace_sentence


def make_NG_list():
    NG_word_list = []
    while True:
        print('NGワードを入力してください。')
        NG_word = input("これ以上必要ないときはそのままエンターを押してください。　＞　")
        if NG_word == '':
            break
        NG_word_list.append(NG_word)
    return NG_word_list


NG_word_list = ['アホ', 'あほ', '阿呆']
replace_word = '<桂三度>'
my_filter = WordFilter(NG_word_list=NG_word_list, replace_word=replace_word)
message_list = []
user_list = []


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template("board.html", message_list=message_list)
    if request.method == 'POST':
        username = request.form['username']
        username = my_filter.censor(username)
        user_count = user_list.count(username) + 1
        user_list.append(username)
        message = request.form['message']
        message = my_filter.censor(message)
        if username == '':
            message_list.append(f'名無しさん:{message}')
            return redirect("/")
        message_list.append(f'{username} [{user_count}]: {message}')
        return redirect("/")


if __name__ == '__main__':
    app.run(debug=True, port=8888)
