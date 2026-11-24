# Assignment 1: Text Stats
# Name: Daile Ryan Go

from test_texts import TEST_TEXT_1, TEST_TEXT_2, TEST_TEXT_3

def space_counter(text): # Supporting the stats
    space_counter = 0
    for text_count_loop in text:
        if text_count_loop == " ":
            space_counter += 1
    return space_counter

def word_frequency_counter(text): # Supporting the stats
    frequency_reader = {}
    alphabet_letters = "abcdefghijklmnopqrstuvwxyz"

     # This loop analyzes the sentences and see if how many unique words are being used.
    for words_repeat in text.split():
        cleaned_word = ""
        for text_count_loop in words_repeat.lower():
            if text_count_loop in alphabet_letters:
                cleaned_word += text_count_loop

        words_repeat = cleaned_word

        if words_repeat == "": 
            continue

        if words_repeat not in frequency_reader:
            frequency_reader[words_repeat] = 1
        else:
            frequency_reader[words_repeat] += 1
    return frequency_reader

def character_count(text):
    text_count = 0

    for text_count_loop in text:
        text_count += 1
    return text_count

def character_count_spaceless(text):
    text_space = character_count(text) - space_counter(text)
    return text_space

def letter_counter(text):
    text_letters_only = 0
    for text_count_loop in text:
        if text_count_loop.isalpha():
            text_letters_only += 1
    return text_letters_only

def vowel_counter(text):
    vowel_count = 0
    for text_count_loop in text:
        if text_count_loop.lower() in "aeiou":
            vowel_count += 1
    return vowel_count

def common_word_counter(frequency_reader):
    highest_count = None
    highest_word = None
    for dictionary_word, dictionary_count in frequency_reader.items(): # This statistics counts how many times a word is used and dictates which word is used often
        if highest_count is None or highest_count < dictionary_count:
            highest_word = dictionary_word
            highest_count = dictionary_count
    return highest_word, highest_count

def total_word_counter(frequency_reader):
    word_count = 0
    for dictionary_word, dictionary_count in frequency_reader.items():
        word_count += dictionary_count
    return word_count

def space_count_statistics(text):
    text_count = character_count(text)
    if text_count > 0:   # REVISED: // I Moved it before the dictionary so it reads first
        space_percentage = (space_counter(text) / text_count) * 100
    else:
        space_percentage = 0
    return space_percentage

def unique_words(frequency_reader):
    return len(frequency_reader)

def common_word(highest_word, highest_count):
    if highest_word is None:
        highest_count_variable = "You have not inputted a word that repeats."
    elif highest_count == 1:
        highest_count_variable = "You have used unique words in your paragraph."
    else:
        highest_count_variable = f"Most common word is == {highest_word} ==, and used {highest_count} times" # // :REVISED 
    return highest_count_variable



def analyze(text):
    frequency_reader = word_frequency_counter(text)
    text_count = character_count(text)
    text_space = character_count_spaceless(text)
    text_letters_only = letter_counter(text)
    vowel_count = vowel_counter(text)
    word_count = total_word_counter(frequency_reader)
    space_percentage = space_count_statistics(text)
    highest_word, highest_count = common_word_counter(frequency_reader)
    highest_count_variable = common_word(highest_word, highest_count)

    statistics_print = { # REVISED: // This is the dictionary for the statistics
        "Character count": text_count,
        "Character count without space": text_space,
        "Character count letters only": text_letters_only,
        "Character count vowels only": vowel_count,
        "Counting words": word_count,
        "Space percentage is": f"{space_percentage:.1f}%",
        "Unique Words": unique_words(frequency_reader),
        "Common words": highest_count_variable, # // :REVISED
    } 
    report_print(statistics_print)

def report_print(statistics_print):
    print("----- This is your statistics -----\n\n") 

    for statistics_name_key, statistics_value in statistics_print.items():
        print(f"{statistics_name_key}: {statistics_value}")

    print("\n\n-------------------------")


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