# Assignment 1: Text Stats
# Name: Daile Ryan Go

from test_texts import TEST_TEXT_1, TEST_TEXT_2, TEST_TEXT_3


def analyze(text):
    text_count = 0
    space_counter = 0
    text_alpha = 0
    vowels_count = 0
    word_count = len(text.split())
    highest_count = None
    highest_word = None
    # alphabet_letters = "abcdefghijklmnopqrstuvwxyz" # REVISED: Changed my strip into this to detect letters and skip symbols
    for text_count_loop in text:
        text_count +=1
        if text_count_loop == " ":
            space_counter += 1

        if text_count_loop.isalpha():
            text_alpha += 1
        if text_count_loop.lower() in "aeiou":
            vowels_count += 1

    frequency_reader = {}

    for words_repeat in text.split(): # This loop analyzes the sentences and see if how many unique words are being used.

        # if words_repeat.lower() not in alphabet_letters: # REVISED: This is the revised version of the line to remove symbols. Is not working and I do not know why

        words_repeat = words_repeat.lower().strip(".,?!:;\"'()[]{}#$@") # This was my old version of disregarding symbols.

        if words_repeat == "": 
            continue

        if words_repeat not in frequency_reader:
            frequency_reader[words_repeat] = 1
        else:
            frequency_reader[words_repeat] += 1

    for dictionary_word, dictionary_count in frequency_reader.items(): # This statistics counts how many times a word is used and dictates which word is used often
        if highest_count is None or highest_count < dictionary_count:
            highest_word = dictionary_word
            highest_count = dictionary_count

    text_space = text_count - space_counter

    if text_count > 0:   # REVISED: // I Moved it before the dictionary so it reads first
        space_percentage = (space_counter / text_count) * 100
    else:
        space_percentage = 0
    if highest_word is None:
        highest_count_variable = "You have not inputted a word that repeats."
    elif highest_count == 1:
        highest_count_variable = "You have used unique words in your paragraph."
    else:
        highest_count_variable = f"Most common word is -- {highest_word} --, and used {highest_count} times" # // :REVISED 


    statistics_print = { # REVISED: // This is the dictionary for the statistics
        "Character count": text_count,
        "Character count without space": text_space,
        "Character count letters only": text_alpha,
        "Character count vowels only": vowels_count,
        "Character count words only": word_count,
        "Space percentage is": f"{space_percentage:.1f}%",
        "Unique Words": len(frequency_reader),
        "Common words": highest_count_variable, # // :REVISED


    } 

    print("----- This is your statistics -----\n\n")  # REVISED: // This is to print the dictionary

    for statistics_name_key, statistics_value in statistics_print.items():
        print(f"{statistics_name_key}: {statistics_value}")

    print("\n\n-------------------------") # It looks just straight stats. Need to be learned more.

# //  This is my old one.
    # # Make this into a dictionary to make it easier\
    # print("Character count:", text_count)
    # print("Character count without space:", text_space)
    # print("Character count letters only: ", text_alpha)
    # print("Character count vowels only: ", vowels_count)
    # print("Character count words only: ", word_count)
    # print(f"Space percentage is: {space_percentage:.1f}%")
    # print(f"Your Unique Words are {len(frequency_reader)}")
    # if highest_word is None:
    #     print("You have not inputted a word that repeats.")
    # elif highest_count is 1: # REVISED: This is a new addition after the submission. My program keeps printing the first word or string it finds and shows as common words despite the whole paragraph using unique words.
    #     print("You have used unique words in your paragraph.") 
    # else:
    #     print(f"Most common word is -- {highest_word} --, and used {highest_count} times")

# //



menu = {
    "1": "Test paragraph 1",
    "2": "Test paragraph 2",
    "3": "Test paragraph 3",
    "4": "Write your own paragraph."
}


while True:
    print("Text Stats")
    for key, label in menu.items():
        print(f"{key}. {label}")
    choice = input("Choose an option: \n Type Exit if you want to exit.\n").strip()

    if choice.lower() == "exit":
        print("Have a good day.")
        print("Thank you")
        break

    if choice not in menu:
        print("------------------------")
        print("Invalid.")
        print("It is not in the menu.")
        print("------------------------")
        continue



    if choice == "1":
        text = TEST_TEXT_1
    elif choice == "2":
        text = TEST_TEXT_2
    elif choice == "3":
        text = TEST_TEXT_3
    elif choice == "4":
        while True:
            text = input("Write here: \n ------------------ \n")
            if text.strip() == "":
                print("Invalid.")
                print("Sentence is required.")
                continue
            break


    analyze(text)
    break