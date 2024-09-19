Number Guessing Game Script Overview
This script implements a graphical user interface (GUI) for a number guessing game using the PyQt6 framework. The game prompts the player to guess a randomly generated number between 1 and 10, with varying levels of difficulty and scoring.

Key Components:
Imports:

The script imports necessary modules from PyQt6 for creating the application, managing layouts, and handling GUI elements.
It also imports randint from the random module to generate random numbers.
Main Application Class: Root

Inherits from QMainWindow, serving as the main window of the application.
The __init__ method initializes the game settings and the user interface.
User Interface Setup: initUI()

Initializes GUI components such as labels, input fields, and buttons.
Arranges these components using a vertical box layout (QVBoxLayout).
Styling: apply_stylesheet()

Defines a custom stylesheet to enhance the visual appearance of the window, including background color, font sizes, and button styles.
Game Initialization: rd()

Attempts to read game state variables (like chances, total score, and current level) from a temporary file (gm.tmp).
If the file is not found, it sets default values.
Game State Update: updasy()

Writes the current game state to the temporary file and updates the displayed labels with the latest values.
Difficulty Level Management: updlvl1()

Adjusts the number of allowed guesses based on the current difficulty level.
Guess Handling: guess()

Retrieves the user's input and compares it to the randomly generated number.
Updates the score and level based on the outcome of the guess.
Provides feedback through the GUI (e.g., "True Guess", "Go Up", "Go Down").
Decrements chances and resets the game state if the player loses.
Application Execution:

The script initializes a QApplication, creates an instance of the Root class, and starts the application event loop.
Conclusion
This script exemplifies how to create an interactive game using PyQt6, combining user input handling, dynamic feedback, and file I/O for state management. The structured approach and clear separation of functionalities make it a good starting point for learning GUI programming and game development in Python.
