# Assignment 1: Text Stats
# Name: Daile Ryan Go

from test_texts import TEST_TEXT_1, TEST_TEXT_2, TEST_TEXT_3
import statistics_texts

def analyze(text):
    frequency_reader = statistics_texts.word_frequency_counter(text)
    text_count = statistics_texts.character_count(text)
    text_space = statistics_texts.character_count_spaceless(text)
    text_letters_only = statistics_texts.letter_counter(text)
    vowel_count = statistics_texts.vowel_counter(text)
    word_count = statistics_texts.total_word_counter(frequency_reader)
    space_percentage = statistics_texts.space_count_statistics(text)
    highest_word, highest_count = statistics_texts.common_word_counter(frequency_reader)
    highest_count_variable = statistics_texts.common_word(highest_word, highest_count)

    statistics_print = { # REVISED: // This is the dictionary for the statistics
        "Character count": text_count,
        "Character count without space": text_space,
        "Character count letters only": text_letters_only,
        "Character count vowels only": vowel_count,
        "Counting words": word_count,
        "Space percentage is": f"{space_percentage:.1f}%",
        "Unique Words": statistics_texts.unique_words(frequency_reader),
        "Common words": highest_count_variable, # // :REVISED
    } 

    report_print(statistics_print)

def report_print(statistics_print):
    print("----- This is your statistics -----\n\n") 

    for statistics_name_key, statistics_value in statistics_print.items():
        print(f"{statistics_name_key}: {statistics_value}")

    print("\n\n-------------------------")

def menu_selection():
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
            return None

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
        return text

text = menu_selection()

if text:
    analyze(text)