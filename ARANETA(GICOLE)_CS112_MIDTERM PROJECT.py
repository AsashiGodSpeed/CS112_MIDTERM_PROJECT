import random  # Import the random module for generating random numbers
import sys  # Import the sys module for system-related functionalities


# Define a function for the one-player game.
def one_plr():
    # Initialize win counts for Player and AI and ties count to 0
    plr_win = 0
    ai_win = 0
    ties = 0

    # Iterate for three rounds.
    for i in range(1, 4):
        # Define the elements and their weaknesses.
        elements = {'f': "Fire", 'w': "Water", 'l': "Leaf", 'e': "Earth", 'a': "Air", 'i': "Ice"}
        element_weakness = {"Fire": ("Air", "Water"), "Water": ("Leaf", "Ice"), "Leaf": ("Fire", "Air"),
                            "Earth": ("Water", "Leaf"), "Air": ("Earth", "Ice"), "Ice": ("Fire", "Earth")}

        # Prompt the player to select an element.
        print("[F] Fire, [W] Water, [L] Leaf, [E] Earth, [A] Air, [I] Ice")
        while True:
            select1 = input("Select your element:").lower()
            if select1 in elements:
                user_element1 = elements[select1]
                print(f"You have chosen {user_element1}")
                element1 = random.choice(list(elements.values()))

                # Determine the weaknesses of the player's chosen element and the AI's randomly selected element
                user_weakness = element_weakness[user_element1]
                ai_weakness = element_weakness[element1]

                # Determine the round outcome.
                if user_element1 in ai_weakness:
                    print(f"The Enemy has chosen {element1}, You Win Round {i}\n")
                    plr_win += 1
                    break
                    # Check if the AI's element has a weakness against the player's element

                elif element1 in user_weakness:
                    print(f"The Enemy has chosen {element1}, You Lose Round {i}\n")
                    ai_win += 1
                    break
                    # If there's no clear weakness, it's a tie
                else:
                    print(f"The Enemy has chosen {element1}, Round {i} is a Tie\n")
                    ties += 1
                    break
            else:
                print("Invalid choice. Please select a valid element.")

        # Determine the game outcome.
        if plr_win > ai_win:
            print(f"You win! {plr_win} win, {ai_win} lost, {ties} tie")
        elif plr_win < ai_win:
            print(f"You lose! {plr_win} win, {ai_win} lost, {ties} tie")
        else:
            print(f"It's a tie! {plr_win} win, {ai_win} lost, {ties} tie")


# Define a function for the two-player game.
def two_plr():
    # Initialize win counts for players 1 and player 2 and ties count to 0
    plr1_win = 0
    plr2_win = 0
    ties = 0

    # Iterate for three rounds.
    for i in range(1, 4):
        # Define the elements and their weaknesses.
        elements = {'f': "Fire", 'w': "Water", 'l': "Leaf", 'e': "Earth", 'a': "Air", 'i': "Ice"}
        element_weakness = {"Fire": ("Air", "Water"), "Water": ("Leaf", "Ice"), "Leaf": ("Fire", "Air"),
                            "Earth": ("Water", "Leaf"), "Air": ("Earth", "Ice"), "Ice": ("Fire", "Earth")}

        # Prompt both players to select elements.
        print("[F] Fire, [W] Water, [L] Leaf, [E] Earth, [A] Air, [I] Ice")
        while True:
            select1 = input("Select your element Player 1: ").lower()
            if select1 in elements:
                break
            else:
                print("Invalid choice. Please select a valid element.")

        # Prints 30 newline to clear the console for player 2's choice.
        print("\n" * 30)

        # Prompt Player 2 to select their element
        while True:
            select2 = input("Select your element Player 2:").lower()

            # Check if both Player 1 and Player 2 selected valid elements
            if select1 in elements and select2 in elements:
                user_element1 = elements[select1]
                print(f"Player 1 has chosen {user_element1}")
                user_element2 = elements[select2]

                # Get weaknesses for both player's elements
                player1_weakness = element_weakness[user_element1]
                player2_weakness = element_weakness[user_element2]

                # Determine the round outcome based on weaknesses
                if user_element1 in player2_weakness:
                    print(f"Player 2 has chosen {user_element2}, Player 1 Wins Round {i}\n")
                    plr1_win += 1
                    break
                    # Check if the AI's element has a weakness against the player's element
                elif user_element2 in player1_weakness:
                    print(f"Player 2 has chosen {user_element2}, Player 2 Wins Round {i}\n")
                    plr2_win += 1
                    break
                    # If there's no clear weakness, it's a tie
                else:
                    print(f"Player 2 has chosen {user_element2}, Round {i} is a Tie\n")
                    ties += 1
                    break
                # If the player's choice is not valid, prompt them to select a valid element
            else:
                print("Invalid choice. Please select a valid element.")

        # Determine the game outcome.
        if plr1_win > plr2_win:
            print(f"Player 1 won! Player 1 won {plr1_win}, Player 2 won {plr2_win}, {ties} tie")
        elif plr1_win < plr2_win:
            print(f"Player 2 won! Player 1 won {plr1_win}, Player 2 won {plr2_win}, {ties} tie")
        else:
            print(f"It's a tie! Player 1 won {plr1_win}, Player 2 won {plr2_win}, {ties} tie")


# Main program starts here.
print("Elemental Clash")
while True:
    versus = int(input("1 Player or 2 Players? Enter [1] if 1P and [2] if 2P: "))
    if versus == 1 or versus == 2:
        break
    else:
        print("Invalid input. Please try again")

# Display the chosen game mode based on the player's input
while True:
    if versus == 1:
        print("You have chosen 1 player")
        break
    elif versus == 2:
        print("You have chosen 2 player")
        break
# Ask the user if they want to see the tutorial
while True:
    Tutorial = input("Do you want to see the tutorial? Y/N: ").upper()
    if Tutorial == 'Y':
        print("\nThere are 6 elements. Fire, Water, Leaf, Earth, Air, Ice\n\n"
              "Fire beats Ice and Leaf\nWater beats Fire and Earth\nLeaf beats Air and Ice"
              "\nEarth beats Fire and Air\nAir beats Leaf and Ice\nIce beats Water and Earth\n")
        Quit = input("Enter Q to exit: ").upper()
        if Quit == 'Q':
            break
    elif Tutorial == 'N':
        break
    else:
        print("Enter only Y or N")

# Check if the game mode is 1 player
if versus == 1:
    while True:
        print("----------------------------------------------------------")
        # Call the one-player game function
        one_plr()
        print("----------------------------------------------------------")
        # Ask if the player wants to play again or exit
        again = input("Do you want to play again? Y/N: ").upper()
        
        # Ensure valid input for playing again or exiting
        while again not in ('Y', 'N'):
            print("Enter only Y or N")
            again = input("Do you want to play again? Y/N: ").upper()
            if again == 'N':
                sys.exit()

# If the game mode is 2 players, enter this block
else:
    while True:
        print("----------------------------------------------------------")
        two_plr()
        print("----------------------------------------------------------")
        # Ask if the player wants to play again or exit
        again = input("Do you want to play again? Y/N: ").upper()
        
        # Ensure valid input for playing again or exiting
        while again not in ('Y', 'N'):
            print("Enter only Y or N")
            again = input("Do you want to play again? Y/N: ").upper()
            if again == 'N':
                sys.exit()
                
