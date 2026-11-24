import statistics_texts
from test_texts import TEST_TEXT_1, TEST_TEXT_2, TEST_TEXT_3

frequency_reader = statistics_texts.word_frequency_counter(TEST_TEXT_1)

assert statistics_texts.character_count(TEST_TEXT_1) == 236
assert statistics_texts.character_count_spaceless(TEST_TEXT_1) == 194
assert statistics_texts.letter_counter(TEST_TEXT_1) == 189
assert statistics_texts.vowel_counter(TEST_TEXT_1) == 74
assert statistics_texts.total_word_counter(frequency_reader) == 43
assert round(statistics_texts.space_count_statistics(TEST_TEXT_1), 1) == 17.8
assert statistics_texts.unique_words(frequency_reader) == 38
assert statistics_texts.common_word_counter(frequency_reader) == ("the", 3)

print("All tests passed")