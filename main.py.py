# Assignment 1: Text Stats
# Name:
#
# Starter code. It runs, but it doesn't handle bad input and it doesn't
# calculate anything yet. Both are your job. Change anything in this file.

# Brings in the three test paragraphs from test_texts.py (same folder).
# Module 2 covers how this works. For now, use them like any variable.
from test_texts import TEST_TEXT_1, TEST_TEXT_2, TEST_TEXT_3


# analyze is a function: a named block of code that runs when it's called.
# The last line of this file calls it with the text the user picked, and
# inside the block that text is in the variable called text.
# Module 2 covers functions properly. For now, all your statistics and your
# report go inside this block (keep them indented).
def analyze(text):
    text_count = 0
    space_counter = 0
    text_alpha = 0
    vowels_count = 0
    word_count = len(text.split())
    for text_count_loop in text:
        if text_count_loop == " ":
            space_counter += 1
        if text_count_loop.isalpha():
            text_alpha += 1
        if text_count_loop.lower() in "aeiou":
            vowels_count += 1
        text_count +=1


    text_space = text_count - space_counter

    print("Character count:", text_count)
    print("Character count without space:", text_space)
    print("Character count letters only: ", text_alpha)
    print("Character count vowels only: ", vowels_count)
    print("Character count words only: ", word_count)
    if text_count > 0:
        space_percentage = (space_counter / text_count) * 100
        print(f"Space percentage is: {space_percentage:.1f}%")
    else:
        print("Space percentage is 0%")



# Menu options: the key is what the user types, the value is what they see
menu = {
    "1": "Test paragraph 1",
    "2": "Test paragraph 2",
    "3": "Test paragraph 3",
}

TEST_TEXT_1 = (
    "Winnipeg sits where the Red and Assiniboine rivers meet. "
    "People have gathered at this spot for thousands of years to trade, "
    "travel and share news. Today the area is called The Forks, "
    "and it is still a busy meeting place in every season."
)

TEST_TEXT_2 = (
    "Order #4471 shipped on 2026-10-02: 3 keyboards ($49.99 each), "
    "12 cables, and 1 monitor. Total: $281.45 (tax included). "
    "Questions? Call 204-555-0187!"
)

TEST_TEXT_3 = "Python is FUN. Really, REALLY fun!"

print("Text Stats")
for key, label in menu.items():
    print(f"{key}. {label}")
choice = input("Choose an option: ")

if choice == "1":
    text = TEST_TEXT_1
elif choice == "2":
    text = TEST_TEXT_2
elif choice == "3":
    text = TEST_TEXT_3

analyze(text)
