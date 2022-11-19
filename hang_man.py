import random

list_words = ["rejects", "subject", "roller", "fighter", "eggplants", "triple"]
hangman_lst = [
    """
_______
|/      |
|      (_)
|      \|/
|       |
|      / \
|
     """,
    """
_______
|/     |
|     (_)
|     \|/
|      |
|     / 
| 
               """,
    """ 
_______
|/      |
|      (_)
|      \|/
|       |
|     
|
               """,
    """
_______
|/      |
|      (_)
|      \|/
|       
|
|
                """,
    """ 
_______
|/     |
|     (_)
|     
|      
|   
|
                """
    ,
    """ 
_______
|/     |
|      
|      
|     
|      
|
               """,
    """
 ______
 |/     
 |      
 |     
 |       
 """]


def hangman():
    print("Welcome to HANGMAN GAME")
    string_to_list(list_words)


def string_to_list(lst: []):
    word_to_guess = random.choice(lst)
    list_of_guessed_word = []
    list_of_guessed_word[:10] = word_to_guess
    length = len(word_to_guess)
    out_put_lst_creation(length, list_of_guessed_word)


def out_put_lst_creation(length: int, lst: []):
    print("-" * length)
    correct_words = []
    for i in range(length):
        correct_words.append("-")
    print(correct_words)
    check_input(lst, correct_words, length)


def letter_found(lst: [], lst2: [], letter: str, length: int):
    found = False
    for i in range(length):
        if lst[i] == letter.lower():
            lst2.pop(i)
            lst2.insert(i, letter)
            found = True
    return found


def letter_not_found(counter, lst: []):
    if counter <= 7:
        print(hangman_lst.pop(7 - counter))
        print(lst)
    elif counter > 7:
        print("Game Over, Hang Man dead..")


def check_input(lst: [], lst2: [], length):
    end_of_game = False
    counter = 0
    while not end_of_game:
        letter = input("Guess the following letters to fill in the blanks\n")
        if letter_found(lst, lst2, letter, length):
            print(lst2)
        else:
            counter += 1
            letter_not_found(counter, lst2)
        if "-" not in lst2:
            end_of_game = True
            print("You win!")
            break


hangman()
