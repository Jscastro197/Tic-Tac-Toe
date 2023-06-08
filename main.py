from flask import Flask, render_template, request, jsonify
from minimax import Computer

app = Flask(__name__)

@app.route('/') # Home page
def hello():
    return render_template('index.html')

@app.route('/make-move', methods=['POST']) # Make a move
def make_move():
    data = request.json
    game_state = data['gameState']
    current_player = data['currentPlayer']
    
    computer = Computer(current_player)
    move = computer.get_move(game_state)
    return jsonify({'move': move})

if __name__ == "__main__":
    app.run(port=8000, debug=True)
