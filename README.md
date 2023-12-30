# Small Python Stuff

Hello! In this repo you'll find a collection of small Python projects I coded. I will add projects over time.


## Projects

### [Command line Card game ("War")](src/card_game/)

#### Description

This is a command line implementation of the classic card game "War". In this two-player game, the deck is divided, and players take turns playing cards. The player with the higher-ranked card wins and takes both cards, and the game continues until one player runs out of cards.

The project includes functionality for handling ties, which leads to a "war" where three additional cards are played, and the player with the higher-ranked fourth card wins all the cards played during the war.

#### Usage

No external dependencies are required. Simply run the `card_game.py` script to start the game.

---

### [File Rename Script](src/file_rename_increment/)

#### Description

This script rename files in a specified folder by adding an incremental suffix. It sorts the files by their last modification time and renames them as "Skärmbild (1).png", "Skärmbild (2).png", and so on. Automated to streamline a recurring file renaming task.

#### Usage

No external dependencies are required. Set the `folder_path` variable to the path of the folder containing the files you want to rename. Run the `file_rename_increment.py` script and it will rename the files in the specified folder.

---

### [Guessing Number Game](src/guess_number/)

#### Description

This is a simple command line number guessing game. The computer generates a random 3-digit number with no repeating digits, and you have to guess the number. After each guess, the computer provides clues (Match, Close, Nope) based on the correctness of your guess. The game continues until you guess the correct number.

#### Usage

No external dependencies are required. Simply run the `guess_number.py` script to start the game.

---

### [Task Tracker using MongoDB](src/task_tracker/)

#### Description

This is a task manager that stores tasks in a MongoDB database. Supports adding, listing, updating task status and deleting tasks.

#### Usage

To run this project, follow these steps:

1. You need MongoDB on you machine. If not yet installed refer to the [official MongoDB installation guide](https://docs.mongodb.com/manual/installation/) for instructions on how to install MongoDB.

2. Make sure to set up your virtual environment.

3. Install `pymongo` using pip:

```shell
python -m pip install pymongo
```

4. Run `main.py` to start the task manager.
   
This will run the application, connecting it to your local MongoDB instance. If needed, customize the MongoDB connection details in `database.py`, e.g. port.


## Clone the repository

```shell
git clone https://github.com/your-username/small-python-stuff.git
cd small-python-stuff/src/{project_folder}
```

Note: Make sure you have Python installed to run the scripts.