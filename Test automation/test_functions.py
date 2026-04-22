from functions import count_word_matches
import pytest

# --- BASIC TEST ---
class TestBasicFunctions:
    @pytest.mark.parametrize("text, target, expected", [
        ("The cat sat on the mat", "cat", 1),
        ("Hello world", "world", 1),
        ("a a a", "a", 3)
    ])
    def test_one_word(self, text, target, expected):
        assert count_word_matches(text, target) == expected

    @pytest.mark.parametrize("text, target, expected", [
        ("Dog dog DOG dOg", "dog", 4),
        ("hello hello HELLO", "hello", 3)
    ])
    def test_ignore_upper_lower_case(self, text, target, expected):
        assert count_word_matches(text, target) == expected

    def test_no_match(self):
        text = "No matches here"
        target = "yes"
        assert count_word_matches(text, target) == 0

    def test_standalone_word(self):
        text = "catcat cat catdog"
        target = "cat"
        assert count_word_matches(text, target) == 1


# --- EDGE CASE TESTING ---
class TestEdgeCases:
    @pytest.mark.parametrize("text, target, expected", [
        ("", "word", 0),
        ("hello world", "", 0),
        ("", "", 0)
    ])
    def test_empty(self, text, target, expected):
        assert count_word_matches(text, target) == expected

    @pytest.mark.parametrize("text, target, expected", [
        ("hello  world", "world", 1),
        ("  cat  ", "cat", 1),
        ("cat,dog cat", "cat", 1)
    ])
    def test_only_spaces(self, text, target, expected):
        assert count_word_matches(text, target) == expected

    def test_single_character(self):
        text = "x y z"
        target = "x"
        assert count_word_matches(text, target) == 1


# --- NEGATIVE TESTING ---
class TestNegativeCases:
    @pytest.mark.parametrize("text, target, expected", [
        (None, "word", 0),
        ("hello world", None, 0),
    ])
    def test_none(self, text, target, expected):
        assert count_word_matches(text, target) == expected

    @pytest.mark.parametrize("text, target, expected", [
        (123, "word", AttributeError),
        ("hello world", 456, AttributeError),
        (["hello", "world"], "world", AttributeError),
        ("hello world", ["world"], AttributeError)
    ])
    def test_attribute_error(self, text, target, expected):
        with pytest.raises(expected):
            count_word_matches(text, target)