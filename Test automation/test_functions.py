from functions import count_word_matches
import pytest

# --- BASIC TEST ---
class TestBasicFunctions:
    def test_one_word(self):
        text = "The cat sat on the mat"
        target = "cat"
        assert count_word_matches(text, target) == 1

    def test_ignore_upper_lower_case(self):
        text = "Dog dog DOG dOg"
        target = "dog"
        assert count_word_matches(text, target) == 4

    def test_one_word_2(self):
        text = "Hello world"
        target = "world"
        assert count_word_matches(text, target) == 1

    def test_ignore_upper_lower_case_2(self):
        text = "hello hello HELLO"
        target = "hello"
        assert count_word_matches(text, target) == 3

    def test_no_match(self):
        text = "No matches here"
        target = "yes"
        assert count_word_matches(text, target) == 0

    def test_standalone_word(self):
        text = "catcat cat catdog"
        target = "cat"
        assert count_word_matches(text, target) == 1

    def test_all_words(self):
        text = "a a a"
        target = "a"
        assert count_word_matches(text, target) == 3


# --- EDGE CASE TESTING ---
class TestEdgeCases:
    def test_empty_text(self):
        text = ""
        target = "word"
        assert count_word_matches(text, target) == 0

    def test_empty_target(self):
        text = "hello world"
        target = ""
        assert count_word_matches(text, target) == 0

    def test_empty_both(self):
        text = ""
        target = ""
        assert count_word_matches(text, target) == 0

    def test_several_spaces(self):
        text = "hello  world"
        target = "world"
        assert count_word_matches(text, target) == 1

    def test_trailing_spaces(self):
        text = "  cat  "
        target = "cat"
        assert count_word_matches(text, target) == 1

    def test_punctuation_marks_no_space(self):
        text = "cat,dog cat"
        target = "cat"
        assert count_word_matches(text, target) == 1

    def test_single_character(self):
        text = "x y z"
        target = "x"
        assert count_word_matches(text, target) == 1


# --- NEGATIVE TESTING ---
class TestNegativeCases:
    def test_no_text(self):
        text = None
        target = "word"
        assert count_word_matches(text, target) == 0

    def test_no_target(self):
        text = "hello world"
        target = None
        assert count_word_matches(text, target) == 0

    def test_attribute_text_error(self):
        text = 123
        target = "word"
        with pytest.raises(AttributeError):
            count_word_matches(text, target)

    def test_attribute_target_error(self):
        text = "hello world"
        target = 456
        with pytest.raises(AttributeError):
            count_word_matches(text, target)

    def test_attribute_textlist_error(self):
        text = ["hello", "world"]
        target = "world"
        with pytest.raises(AttributeError):
            count_word_matches(text, target)

    def test_attribute_targetlist_error(self):
        text = "hello world"
        target = ["world"]
        with pytest.raises(AttributeError):
            count_word_matches(text, target)