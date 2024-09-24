import random

# Main function that manages the flow of the program
def main():
    print("Hello World")  # Start of the page
    print("Welcome to Kodigo_90.cl")
    
    user_registered = False
    username = ""
    password = ""

    while True:
        option_web = show_main_menu()

        if option_web == "1":
            if user_registered:
                log_in(username, password)
            else:
                print("No registered users. Please register first.")
        elif option_web == "2":
            username, password = register_user()
            user_registered = True
        elif option_web == "3":
            print("Exiting the program.")
            break  # Exit the program

# Function to display the main menu
def show_main_menu():
    print("1: Log in")
    print("2: Register User")
    print("3: Exit")
    return input("Select an option: ")

# Function to register a user
def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    print(f"User {username} registered successfully.")
    return username, password

# Function to log in
def log_in(username, password):
    while True:
        entered_password = input("Password: ")
        if entered_password == password:
            print(f"Welcome, {username}! You have successfully logged in :)")
            interact_with_user(username)
            break
        else:
            print("Incorrect password, please try again: ")

# Function to interact with the user once logged in
def interact_with_user(username):
    while True:
        print(f"\t\tWhat would you like to do, {username}?")
        print("1: Learn what and how you can use this website")
        print("2: Play a game")
        print("3: Calculator")
        print("4: Register, Update and Show Inventory")
        print("5: Online Supermarket")
        print("6: Calculate an average")
        print("7: Log out")

        option_content = input("Select an option: ")
        if option_content == "1":
            show_site_info()
            print('''

Welcome to Kodigo_90.cl! Our website is an interactive platform designed for users to dive into the exciting world of programming. 
Created by Ignacio Tapia, this platform offers a wide range of resources and tools that allow users to learn, practice, and enjoy programming in a fun and accessible way. 
From detailed tutorials to challenging games and a funny calculator, Kodigo_90.cl offers something for everyone. Do you want to learn the basics of Python? You're in the right place! 
Need help solving a programming problem? Our resources are here to help you! 
Moreover, our website is ideal for businesses and individual users looking to experience programming work and explore new opportunities. Whether you're looking to develop technical skills, expand your creativity, or just have a good time, 
Kodigo_90.cl has everything you need and more! Join our community today and start your journey towards programming mastery. You won’t regret it!

Press Enter to return to the main menu...
''')
            input()  # Wait for the user to press Enter
        elif option_content == "2":
            play_game()
            while True:
                print("\t\tWHAT GAME WOULD YOU LIKE TO PLAY???")
                print("1: Heads or Tails")
                print("2: Penalty")
                print("3: Rock, Paper, Scissors")
                print("4: Tic-Tac-Toe")
                print("5: General Knowledge")
                print("6: Return to main menu")

                game_option = input("Choose a game (1, 2, 3, 4, or 5): or '6' to return to the Content Menu: ")

                if game_option == "1":  # Heads or Tails
                    while True:
                        coin_question = input("Choose Heads or Tails (Heads/Tails): or type 'Exit' to return to the game menu: ").capitalize()
                        if coin_question == "Exit":
                            break
                        if coin_question not in ["Heads", "Tails"]:
                            print("Error: Please choose one of the 2 options shown (Heads/Tails)")
                            continue  # Restart the loop if the input is invalid

                        coin = random.choice(["Heads", "Tails"])  # Simulate coin toss
                        print(f"The coin landed on {coin}")

                        if coin_question == coin:
                            print("You won! :)")
                        else:
                            print("You lost... better luck next time")
                        while True:

                            flip_again = input("Do you want to flip the coin again? (yes/no): ").lower()
                        
                            if flip_again == "yes":
                                break  # Exit this loop and ask Heads or Tails again
                        
                            elif flip_again == "no":
                                break  # Exit both loops and return to the game menu
                            else:
                                print("Error: Please choose one of the 2 options shown")
                                continue
                        if flip_again == "no":
                                break
                
                elif game_option == "2":  # Penalties

                    while True:
                        teams = ["Real Madrid", "Manchester City"]
                        while True:  # Loop to ensure the user selects a valid option
                            print("Choose a team (or type 'Exit' to return to the game menu):")
                            print("\n".join(f"{i + 1}: {team}" for i, team in enumerate(teams)))
                            chosen_option = input("Enter the number corresponding to the team or 'Exit': ")

                            if chosen_option.lower() == "exit":
                                return_option = "exit"
                                break  # Return to the game menu
                            elif chosen_option in ["1", "2"]:
                                chosen_team = teams[int(chosen_option) - 1]
                                print(f"Chosen team: {chosen_team}")
                                break
                            else:
                                print("Error: You must choose a valid option (1 for Real Madrid, 2 for Manchester City or 'Exit').")
                                continue

                        if chosen_option.lower() == "exit":
                            break

                        computer_team = teams[1] if chosen_team == teams[0] else teams[0]
                        print(f"AI Team: {computer_team}")

                        print("THE PENALTY SHOOTOUT BEGINS!!!")

                        while True:
                            if chosen_team == "Real Madrid":
                                user_penalty = input("Vinicius Junior will take the penalty, where do you want him to shoot (Left or Right)? (or type 'Exit' to return to the game menu): ").capitalize()
                                if user_penalty == "Exit":
                                    return_option = "exit"
                                    break
                                if user_penalty not in ["Left", "Right"]:
                                    print("Error: You can only choose Left or Right")
                                    continue
                                penalty_shot = random.choice(["Left", "Right"])
                                print(f"Vinicius shot to the {user_penalty} and...")

                                if user_penalty != penalty_shot:
                                    print("Goal! Vinicius scored a fantastic penalty. Real Madrid wins!")
                                else:
                                    print("Goalkeeper Ederson guessed the penalty. Bad luck! Manchester City wins.")

                            elif chosen_team == "Manchester City":
                                user_penalty = input("Kevin De Bruyne will take the penalty, where do you want him to shoot (Left or Right)? (or type 'Exit' to return to the game menu): ").capitalize()
                                if user_penalty == "Exit":
                                    return_option = "exit"
                                    break
                                if user_penalty not in ["Left", "Right"]:
                                    print("Error: You can only choose Left or Right")
                                    continue
                                penalty_shot = random.choice(["Left", "Right"])
                                print(f"De Bruyne shot to the {user_penalty} and...")

                                if user_penalty != penalty_shot:
                                    print("Goal! De Bruyne scored a fantastic penalty. Manchester City wins!")
                                else:
                                    print("Goalkeeper Courtois guessed the penalty. Bad luck! Real Madrid wins.")

                            # After the penalty, offer the option to return to the menu
                            return_option = input("Do you want to play again or return to the game menu? (type 'Again' to play again or 'Exit' to return to the game menu): ").lower()
                            if return_option == "exit":
                                break
                        if return_option == "exit":
                            break

                elif game_option == "3":
                    options = ["rock", "paper", "scissors"]

                    while True:
                        computer_choice = random.choice(options)

                        user_choice = input("Choose rock, paper, or scissors: ").lower()
                        while user_choice not in options:
                            user_choice = input("Please choose rock, paper, or scissors: ").lower()

                        print(f"You chose: {user_choice}")
                        print(f"The computer chose: {computer_choice}")

                        if user_choice == computer_choice:
                            print("It's a tie")
                        elif (user_choice == "rock" and computer_choice == "scissors") or \
                            (user_choice == "paper" and computer_choice == "rock") or \
                            (user_choice == "scissors" and computer_choice == "paper"):
                            print("You win")
                        else:
                            print("You lose")

                        play_again = input("Do you want to play again? (yes/no): ").lower()
                        if play_again != "yes":
                            break

                elif game_option == "4":

                    def print_board(board):
                        # Function to print the board
                        for row in board:
                            print(" | ".join(row))
                            print("-" * 9)

                    def check_winner(board, player):
                        # Check rows
                        for row in board:
                            if all(square == player for square in row):
                                return True
                        # Check columns
                        for col in range(3):
                            if all(board[row][col] == player for row in range(3)):
                                return True
                        # Check diagonals
                        if all(board[i][i] == player for i in range(3)) or \
                        all(board[i][2 - i] == player for i in range(3)):
                            return True
                        return False

                    def board_full(board):
                        # Function to check if the board is full (draw)
                        for row in board:
                            if " " in row:
                                return False
                        return True

                    # Initialize an empty board
                    board = [[" " for _ in range(3)] for _ in range(3)]
                    players = ['X', 'O']
                    turn = 0  # Start with player X

                    # Main game loop
                    while True:
                        print_board(board)
                        print(f"Player {players[turn]}'s turn")

                        # Ask for row and column with an option to exit
                        row = input("Enter the row number (0, 1, or 2) or 'Exit' to return to the game menu: ").lower()
                        if row == "exit":
                            print("Exiting the game...")
                            break
                        if row not in ["0", "1", "2"]:
                            print("Error: You must choose a number between 0, 1, and 2 or 'Exit'.")
                            continue

                        column = input("Enter the column number (0, 1, or 2) or 'Exit' to return to the game menu: ").lower()
                        if column == "exit":
                            print("Exiting the game...")
                            break
                        if column not in ["0", "1", "2"]:
                            print("Error: You must choose a number between 0, 1, and 2 or 'Exit'.")
                            continue

                        row = int(row)
                        column = int(column)

                        # Check if the square is empty
                        if board[row][column] == " ":
                            board[row][column] = players[turn]  # Place the current player's symbol
                        else:
                            print("That square is already occupied. Try again.")
                            continue

                        # Check if there is a winner
                        if check_winner(board, players[turn]):
                            print_board(board)
                            print(f"Player {players[turn]} has won!")
                            break

                        # Check if the board is full (draw)
                        if board_full(board):
                            print_board(board)
                            print("It's a draw!")
                            break
                        
                        # Switching turns
                        turn = (turn + 1) % 2  # Switch between 0 (Player X) and 1 (Player O)

                elif game_option == "5":
                    print("\tWhich subject do you want to choose?")
                    print("1: History")
                    print("2: Mathematics")
                    print("3: Language")
                    print("4: Return to the main menu")

                    subject_option = input("Choose a number for the subject you want to take the exam (or '4' to exit): ")

                    if subject_option == "4":
                        break  # Return to the main menu

                    if subject_option == "1":  # History exam
                        repeat_exam = True
                        while repeat_exam:
                            print('''You have chosen History, now I will explain the exam rules.

                    The History exam contains questions about World War II.
                    You will have 10 questions, and the difficulty will increase. At the end,
                    your score will be displayed. Good luck!

                    Press Enter to start the exam.''')
                            input()

                            score = 0

                            # History questions
                            while True:
                                print("1) When did World War II end?")
                                print("a) 1947")
                                print("b) 1944")
                                print("c) 1945")
                                print("d) 1950")

                                answer1_history = input(" ")

                                if answer1_history.lower() in ["a", "b", "c", "d"]:
                                    if answer1_history.lower() == "c":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("2) Who was the leader of Nazi Germany during World War II?")
                                print("a) Benito Mussolini")
                                print("b) Ronald Reagan")
                                print("c) Adolf Hitler")
                                print("d) Franklin D. Roosevelt")

                                answer2_history = input(" ")

                                if answer2_history.lower() in ["a", "b", "c", "d"]:
                                    if answer2_history.lower() == "c":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("3) What was the name of the project to develop the atomic bomb in the United States?")
                                print("a) Manhattan Project")
                                print("b) Mercury Project")
                                print("c) Manhattan Beach Project")
                                print("d) Silverback Project")

                                answer3_history = input(" ")

                                if answer3_history.lower() in ["a", "b", "c", "d"]:
                                    if answer3_history.lower() == "a":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("4) What was the military operation that marked the beginning of the liberation of Western Europe by the Allies?")
                                print("a) Operation Barbarossa")
                                print("b) Operation Overlord")
                                print("c) Operation Torch")
                                print("d) Operation Market Garden")

                                answer4_history = input(" ")

                                if answer4_history.lower() in ["a", "b", "c", "d"]:
                                    if answer4_history.lower() == "b":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("5) What was the longest battle of World War II?")
                                print("a) Battle of Stalingrad")
                                print("b) Battle of Normandy")
                                print("c) Battle of the Atlantic")
                                print("d) Battle of the Bulge")

                                answer5_history = input(" ")

                                if answer5_history.lower() in ["a", "b", "c", "d"]:
                                    if answer5_history.lower() == "c":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("6) What was the name of the plane that dropped the first atomic bomb on Hiroshima?")
                                print("a) Enola Gay")
                                print("b) Bockscar")
                                print("c) Memphis Belle")
                                print("d) Spirit of St. Louis")

                                answer6_history = input(" ")

                                if answer6_history.lower() in ["a", "b", "c", "d"]:
                                    if answer6_history.lower() == "a":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("7) At which conference was the partition of Germany decided after the war?")
                                print("a) Yalta Conference")
                                print("b) Tehran Conference")
                                print("c) Potsdam Conference")
                                print("d) San Francisco Conference")

                                answer7_history = input(" ")

                                if answer7_history.lower() in ["a", "b", "c", "d"]:
                                    if answer7_history.lower() == "a":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("8) Which country suffered the most casualties during World War II?")
                                print("a) United States")
                                print("b) Germany")
                                print("c) Japan")
                                print("d) Soviet Union")

                                answer8_history = input(" ")

                                if answer8_history.lower() in ["a", "b", "c", "d"]:
                                    if answer8_history.lower() == "d":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("9) Which US general was nicknamed 'Old Blood and Guts' during World War II?")
                                print("a) Dwight D. Eisenhower")
                                print("b) George S. Patton")
                                print("c) Douglas MacArthur")
                                print("d) Omar Bradley")

                                answer9_history = input(" ")

                                if answer9_history.lower() in ["a", "b", "c", "d"]:
                                    if answer9_history.lower() == "b":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("10) What was the name of the German battleship sunk by the British in 1941 that was one of the largest battleships ever built?")
                                print("a) Bismarck")
                                print("b) Tirpitz")
                                print("c) Scharnhorst")
                                print("d) Gneisenau")

                                answer10_history = input(" ")

                                if answer10_history.lower() in ["a", "b", "c", "d"]:
                                    if answer10_history.lower() == "a":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            print("Final score:", score)

                            if score <= 3:
                                print("You have little knowledge of World War II, try studying more.")
                            elif score <= 7:
                                print("You have some knowledge of World War II, you're close to being an expert.")
                            elif score <= 9:
                                print("You have a lot of knowledge of World War II, you could teach history!")
                            elif score == 10:
                                print("You're a genius! You must have a master's degree in history.")

                            while True:
                                final_option = input("Do you want to retake the exam (type 'retake') or return to the game menu (type 'exit')?: ").lower()
                                if final_option == "retake":
                                    break  # Retake the exam
                                elif final_option == "exit":
                                    repeat_exam = False  # Do not retake, exit to the menu
                                    break  # Return to the main menu
                                else:
                                    print("Invalid option. Type 'retake' or 'exit'.")

                    elif subject_option == "2":  # Mathematics Exam
                        repeat_exam = True
                        while repeat_exam:
                            print('''You have chosen Mathematics, now I will explain the exam rules.

                    The Mathematics exam contains 10 questions with varying levels of difficulty.
                    As you progress, the questions will become more difficult. Good luck!

                    Press Enter to start the exam.''')
                            input()

                            score = 0

                            # Mathematics Questions
                            while True:
                                print("1) What is the value of 8 + 8?")
                                print("a) 2")
                                print("b) 18")
                                print("c) 16")
                                print("d) 14")

                                answer1_math = input(" ")

                                if answer1_math.lower() in ["a", "b", "c", "d"]:
                                    if answer1_math.lower() == "c":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("2) What is the result of 9 - 3?")
                                print("a) 3")
                                print("b) 5")
                                print("c) 6")
                                print("d) 9")

                                answer2_math = input(" ")

                                if answer2_math.lower() in ["a", "b", "c", "d"]:
                                    if answer2_math.lower() == "c":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("3) What is the result of 3^2?")
                                print("a) 5")
                                print("b) 6")
                                print("c) 8")
                                print("d) 9")

                                answer3_math = input(" ")

                                if answer3_math.lower() in ["a", "b", "c", "d"]:
                                    if answer3_math.lower() == "d":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("4) What is the square root of 144?")
                                print("a) 10")
                                print("b) 12")
                                print("c) 14")
                                print("d) 16")

                                answer4_math = input(" ")

                                if answer4_math.lower() in ["a", "b", "c", "d"]:
                                    if answer4_math.lower() == "b":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("5) What is the result of the integral of 2x dx?")
                                print("a) x^2 + C")
                                print("b) 2x + C")
                                print("c) x^2 + 2")
                                print("d) 2x^2 + C")

                                answer5_math = input(" ")

                                if answer5_math.lower() in ["a", "b", "c", "d"]:
                                    if answer5_math.lower() == "a":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("6) What is the value of π^2 / 6?")
                                print("a) 1.644")
                                print("b) 2")
                                print("c) 3")
                                print("d) 0.5")

                                answer6_math = input(" ")

                                if answer6_math.lower() in ["a", "b", "c", "d"]:
                                    if answer6_math.lower() == "a":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("7) What is a prime number?")
                                print("a) A number divisible only by itself and 1")
                                print("b) A number divisible by 2")
                                print("c) A number that is a perfect square")
                                print("d) A number that is odd")

                                answer7_math = input(" ")

                                if answer7_math.lower() in ["a", "b", "c", "d"]:
                                    if answer7_math.lower() == "a":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("8) What is the value of the Fourier series for a square wave function with a period of 2π?")
                                print("a) 0")
                                print("b) 4/π * Σ (1/n) sin(nx)")
                                print("c) 2π")
                                print("d) Infinity")

                                answer8_math = input(" ")

                                if answer8_math.lower() in ["a", "b", "c", "d"]:
                                    if answer8_math.lower() == "b":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("9) What is the value of π squared?")
                                print("a) 6.283")
                                print("b) 3.141")
                                print("c) 9.869")
                                print("d) 7.389")

                                answer9_math = input(" ")

                                if answer9_math.lower() in ["a", "b", "c", "d"]:
                                    if answer9_math.lower() == "c":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("10) Solve the time-independent Schrödinger equation for a particle in a one-dimensional box.")
                                print("a) Ψ(x) = A * sin(kx)")
                                print("b) Ψ(x) = B * e^(ikx)")
                                print("c) Ψ(x) = A * cos(kx)")
                                print("d) Ψ(x) = 0")

                                answer10_math = input(" ")

                                if answer10_math.lower() in ["a", "b", "c", "d"]:
                                    if answer10_math.lower() == "a":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            print("Final score:", score)

                            if score <= 3:
                                print("You have little knowledge of Mathematics, try studying more.")
                            elif score <= 7:
                                print("You have some knowledge of Mathematics, you're close to being an expert.")
                            elif score <= 9:
                                print("You have a lot of knowledge of Mathematics, you could teach math!")
                            elif score == 10:
                                print("You're a genius! You must have a master's degree in Mathematics.")

                            while True:
                                final_option = input("Do you want to retake the exam (type 'retake') or return to the game menu (type 'exit')?: ").lower()
                                if final_option == "retake":
                                    break  # Retake the exam
                                elif final_option == "exit":
                                    repeat_exam = False  # Do not retake, exit to the menu
                                    break  # Exit to the main menu
                                else:
                                    print("Invalid option. Type 'retake' or 'exit'.")
                                    
                    elif subject_option == "3":  # Language Exam
                        repeat_exam = True
                        while repeat_exam:
                            print('''You have chosen Language, now I will explain the exam rules.

                    The Language exam contains 10 questions with varying levels of difficulty.
                    As you progress, the questions will become more difficult. Good luck!

                    Press Enter to start the exam.''')
                            input()

                            score = 0

                            # Language Questions
                            while True:
                                print("1) Which word is correct?")
                                print("a) Haya")
                                print("b) Haiga")
                                print("c) Ayá")
                                print("d) Haigae")

                                answer1_language = input(" ")

                                if answer1_language.lower() in ["a", "b", "c", "d"]:
                                    if answer1_language.lower() == "a":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("2) What is the plural of 'café'?")
                                print("a) Cafeses")
                                print("b) Cafés")
                                print("c) Caféses")
                                print("d) Café")

                                answer2_language = input(" ")

                                if answer2_language.lower() in ["a", "b", "c", "d"]:
                                    if answer2_language.lower() == "b":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("3) What is a noun?")
                                print("a) A word that describes an action")
                                print("b) A word that names people, places, or things")
                                print("c) A word that modifies a verb")
                                print("d) A word that indicates a relation")

                                answer3_language = input(" ")

                                if answer3_language.lower() in ["a", "b", "c", "d"]:
                                    if answer3_language.lower() == "b":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("4) What kind of word is 'quickly'?")
                                print("a) Verb")
                                print("b) Adjective")
                                print("c) Adverb")
                                print("d) Noun")

                                answer4_language = input(" ")

                                if answer4_language.lower() in ["a", "b", "c", "d"]:
                                    if answer4_language.lower() == "c":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("5) Which rhetorical device involves the repetition of sounds at the beginning of consecutive words?")
                                print("a) Alliteration")
                                print("b) Metaphor")
                                print("c) Hyperbole")
                                print("d) Simile")

                                answer5_language = input(" ")

                                if answer5_language.lower() in ["a", "b", "c", "d"]:
                                    if answer5_language.lower() == "a":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("6) Which literary device exaggerates a characteristic?")
                                print("a) Simile")
                                print("b) Metaphor")
                                print("c) Hyperbole")
                                print("d) Antithesis")

                                answer6_language = input(" ")

                                if answer6_language.lower() in ["a", "b", "c", "d"]:
                                    if answer6_language.lower() == "c":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("7) What is the structure of a sonnet?")
                                print("a) Two quatrains and two tercets")
                                print("b) Three quatrains and a couplet")
                                print("c) Four stanzas of four verses")
                                print("d) A free verse and a rhymed one")

                                answer7_language = input(" ")

                                if answer7_language.lower() in ["a", "b", "c", "d"]:
                                    if answer7_language.lower() == "a":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("8) What is metonymy?")
                                print("a) The use of one term with the meaning of another by contiguity")
                                print("b) Comparing two things using 'like'")
                                print("c) Exaggerating a quality")
                                print("d) Contrasting two opposite ideas")

                                answer8_language = input(" ")

                                if answer8_language.lower() in ["a", "b", "c", "d"]:
                                    if answer8_language.lower() == "a":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("9) Who is the author of 'Don Quixote'?")
                                print("a) Miguel de Cervantes")
                                print("b) William Shakespeare")
                                print("c) Gabriel García Márquez")
                                print("d) Pablo Neruda")

                                answer9_language = input(" ")

                                if answer9_language.lower() in ["a", "b", "c", "d"]:
                                    if answer9_language.lower() == "a":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            while True:
                                print("10) What is the technical term for altering the logical order of words in a sentence?")
                                print("a) Ellipsis")
                                print("b) Anaphora")
                                print("c) Hyperbaton")
                                print("d) Metaphor")

                                answer10_language = input(" ")

                                if answer10_language.lower() in ["a", "b", "c", "d"]:
                                    if answer10_language.lower() == "c":
                                        score += 1.0
                                    break
                                else:
                                    print("Please enter the corresponding letter for your answer:")

                            print("Final score:", score)

                            if score <= 3:
                                print("You have little knowledge of Language, try studying more.")
                            elif score <= 7:
                                print("You have some knowledge of Language, you're close to being an expert.")
                            elif score <= 9:
                                print("You have a lot of knowledge of Language, you could teach Language!")
                            elif score == 10:
                                print("You're a genius! You must have a master's degree in Language.")

                            while True:
                                final_option = input("Do you want to retake the exam (type 'retake') or return to the game menu (type 'exit')?: ").lower()
                                if final_option == "retake":
                                    break  # Retake the exam
                                elif final_option == "exit":
                                    repeat_exam = False  # Do not retake, exit to the menu
                                    break  # Exit to the main menu
                                else:
                                    print("Invalid option. Type 'retake' or 'exit'.")

                elif game_option == "6":
                    break
        elif option_content == "3":
            calculator()
            while True:
                try:
                    number = int(input("Enter the first number: "))
                    n2 = int(input("Enter another number: "))
                except ValueError:
                    print("Error: You must enter an integer")
                    continue

                op = input("What operation would you like to perform? (+, -, *, /, //, **): ")
                if op == "+":
                    print("Expression:", number, op, n2, "=", (number + n2))
                elif op == "-":
                    print("Expression:", number, op, n2, "=", (number - n2))
                elif op == "*":
                    print("Expression:", number, op, n2, "=", (number * n2))
                elif op == "/":
                    if n2 != 0:  # Ensure the second number is not zero to avoid division by zero
                        print("Expression:", number, op, n2, "=", (number / n2))
                    else:
                        print("Error: Division by zero is not allowed")
                elif op == "//":
                    if n2 != 0:
                        print("Expression:", number, op, n2, "=", (number // n2))
                    else:
                        print("Error: Division by zero is not allowed")
                elif op == "**":
                    print("Expression:", number, op, n2, "=", (number ** n2))
                else:
                    print("Invalid operator")

                if input("Would you like to perform another operation? (yes/no): ").lower() != "yes":
                    break

        elif option_content == "4":
            manage_inventory()

            # Code to manage an online store
            import json
            import os

            FILE_PATH = 'inventory.json'

            def load_inventory():
                inventory = {}
                if os.path.exists(FILE_PATH):
                    with open(FILE_PATH, mode='r') as file:
                        inventory = json.load(file)
                return inventory

            def save_inventory(inventory):
                with open(FILE_PATH, mode='w') as file:
                    json.dump(inventory, file, indent=4)

            def register_product(inventory):
                name = input("Product name: ")
                while True:
                    try:
                        price = float(input("Product price: "))
                        break
                    except ValueError:
                        print("Error: The price must be a number.")
                quantity = int(input("Product quantity: "))
                if name in inventory:
                    print("Product already registered. Use the update option to modify it.")
                else:
                    inventory[name] = {'price': price, 'quantity': quantity}
                    save_inventory(inventory)
                    print(f"Product '{name}' registered successfully with price {price} and quantity {quantity}.")

            def update_inventory(inventory):
                name = input("Name of the product to update: ")
                if name in inventory:
                    while True:
                        try:
                            price = float(input("New product price: "))
                            break
                        except ValueError:
                            print("Error: The price must be a number.")
                    quantity = int(input("New product quantity: "))
                    inventory[name] = {'price': price, 'quantity': quantity}
                    save_inventory(inventory)
                    print(f"Product '{name}' updated successfully.")
                else:
                    print("Product not found.")

            def show_inventory(inventory):
                if inventory:
                    print("+--------------------+----------+----------+")
                    print("| Name               | Price    | Quantity |")
                    print("+--------------------+----------+----------+")
                    for name, details in inventory.items():
                        print(f"| {name:<18} | {details['price']:<8.2f} | {details['quantity']:<8} |")
                    print("+--------------------+----------+----------+")
                else:
                    print("The inventory is empty.")

            def main():
                inventory = load_inventory()

                while True:
                    print("Menu Options")
                    print("\t1. Register product")
                    print("\t2. Update inventory")
                    print("\t3. Show inventory")
                    print("\t4. Exit the application")
                    option = input("Select an option: ")

                    if option == '1':
                        register_product(inventory)
                    elif option == '2':
                        update_inventory(inventory)
                    elif option == '3':
                        show_inventory(inventory)
                    elif option == '4':
                        print("Exiting the application :)")
                        break
                    else:
                        print("Invalid option, please try again.")

            if __name__ == "__main__":
                main()

        elif option_content == "5":
            online_supermarket()
            print("Welcome to Kodigo's online supermarket :)")

            basket = []

            # Available products and their prices
            products = {
                1: ("Rice", 1000),
                2: ("Pasta", 800),
                3: ("Beef", 500),
                4: ("Milk", 300),
                5: ("Eggs", 200)
            }

            while True:
                print("\nMenu:")
                print("1. Add products")
                print("2. View basket")
                print("3. View total")
                print("4. Pay")

                try:
                    option = int(input("Select an option: "))

                    if option == 1:
                        while True:
                            print("\nAvailable products:")
                            for key, value in products.items():
                                print(f"{key}. {value[0]} - ${value[1]}")

                            try:
                                product_option = int(input("Select the number of the product you want to buy: "))
                                if product_option in products:
                                    quantity = int(input(f"How many {products[product_option][0]} would you like to buy?: "))
                                    if quantity > 0:
                                        basket.append((products[product_option][0], products[product_option][1], quantity))
                                        print(f"{products[product_option][0]} x{quantity} added to the basket.")
                                    else:
                                        print("Quantity must be greater than zero. Please try again.")
                                else:
                                    print("Invalid option. Please select a valid number.")
                            except ValueError:
                                print("Invalid input. Please enter a number.")

                            another_purchase = input("Would you like to add another product? (yes/no): ").strip().lower()
                            if another_purchase == "no":
                                break

                    elif option == 2:
                        if basket:
                            print("\nShopping basket:")
                            for product in basket:
                                print(f"{product[0]} x{product[2]} - ${product[1]} each")
                        else:
                            print("The basket is empty.")

                    elif option == 3:
                        total = sum(product[1] * product[2] for product in basket)
                        print(f"\nTotal to pay: ${total}")

                    elif option == 4:
                        total = sum(product[1] * product[2] for product in basket)
                        if basket:
                            print(f"\nTotal to pay: ${total}")
                            print("Processing payment...")
                            print("Thank you for your purchase. Have a great day!")
                        else:
                            print("Your basket is empty, you cannot pay.")
                        break

                    else:
                        print("Invalid option. Please select a valid number.")

                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif option_content == "6":
          
            # Function to calculate the average of a list of numbers
            def calculate_average(numbers):
                if len(numbers) == 0:
                    return 0
                return sum(numbers) / len(numbers)

            # Ask the user to input numbers
            print("Enter the numbers to calculate the average. Type 'q' to finish.")

            numbers = []
            while True:
                entry = input("Enter a number (or 'q' to finish): ")
                if entry.lower() == 'q':
                    break
                try:
                    number = float(entry)
                    numbers.append(number)
                except ValueError:
                    print("Invalid input. Please enter a number or 'q' to finish.")

            # Calculate and display the average
            average = calculate_average(numbers)
            print(f"The average of the entered numbers is: {average:.2f}")


        elif option_content == "7":
            print("Logging out...")
            break

# Function to display site information
def show_site_info():
    print('''Welcome to Kodigo_90.cl! Our website is an interactive platform designed for users to 
    dive into the exciting world of programming. 
    Created by Ignacio Tapia, this platform offers a wide range of resources and tools 
    that allow users to learn, practice, and enjoy programming in a fun and accessible way.''')

# Function to play a game (you can implement the game from your original code here)
def play_game():
    print("You can implement the game you have in your original code here.")

# Function for the calculator
def calculator():
    print("Implement calculator here.")

# Function to manage inventory
def manage_inventory():
    print("Function to register and show inventory.")

# Function for the online supermarket
def online_supermarket():
    print("Implement the online supermarket logic here.")

# Function to calculate averages
def calculate_average():
    print("Average calculator implemented here.")

if __name__ == "__main__":
    main()

