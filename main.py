from flask import Flask, render_template
from minimax import Computer, HumanPlayer

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template ('index.html')


if __name__ == "__main__":
    x_player = Computer('X')
    o_player = HumanPlayer('O')
    app.run(port=8000, debug=True)


