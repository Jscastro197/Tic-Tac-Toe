# Tic-Tac-Toe Game
![](../static/proof.gif)
This repository contains a simple implementation of the Tic-Tac-Toe game.

## Clone the Repository

To clone this repository, run the following command in your terminal:
 ```
  git clone https://github.com/Jscastro197/Tic-Tac-Toe.git
  ```


## Setting up the Development Environment

1. Change your working directory to the cloned repository:


 ```
  cd Tic-Tac-Toe
  ```


2. Create a virtual environment using the following command:

- Windows:

  ```
  py -3 -m venv .venv
  ```

- macOS/Linux:

  ```
  python3 -m venv .venv
  ```

3. Activate the virtual environment:

- Windows:

  ```
  . .venv/Scripts/activate
  ```

- macOS/Linux:

  ```
  source .venv/bin/activate
  ```

4. Install the required dependencies:


  ```
  pip install -r requirements.txt
  ```


## Running the Application

1. Set the Flask app environment variable:

- Windows:

  ```
  set FLASK_APP=main.py
  ```

- macOS/Linux:

  ```
  export FLASK_APP=main.py
  ```

2. Start the Flask application:


  ```
  flask --app main run --debug
  ```


The application will be accessible at [http://localhost:5000](http://localhost:5000) in your browser.

3. Play the Tic-Tac-Toe game by following the on-screen instructions.

## Additional Information

- If you encounter any issues or want to contribute, please open an issue or submit a pull request on the [GitHub repository](https://github.com/Jscastro197/Tic-Tac-Toe).
