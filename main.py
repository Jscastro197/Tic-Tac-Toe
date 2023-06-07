from flask import Flask, render_template
from minimax import minimax, computer, human

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template ('index.html')


if __name__ == "__main__":
    x_player = computer('X')
    o_player = human('O')
    app.run(port=8000, debug=True)


