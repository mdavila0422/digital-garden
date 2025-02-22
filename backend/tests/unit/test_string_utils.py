import backend.app.utils.string_utils as string_utils
import pytest
    
def test_string_below_max_length():
    """
    Test a string that is shorter than the max length.
    The string should be returned unchanged.
    """
    assert string_utils.string_truncator("Hello, world!", 20) == "Hello, world!"
    assert string_utils.string_truncator("Hello, world!", 20, True) == "Hello, world!"
    
def test_string_no_word_boundary():
    """
    Test a string that has no word boundaries within the max length.
    The string should be truncated to the max length and an ellipsis appended.
    """
    assert string_utils.string_truncator("T"*21, 10) == "T"*10 + "..."
    assert string_utils.string_truncator("T"*21, 10, True) == "T"*10 + "..."
    
    
def test_string_with_spaces():
    """
    Test a string that has tabs and multiple spaces within the max length.
    The string should be truncated to the max length and an ellipsis appended.
    """
    assert string_utils.string_truncator("The  quick    brown    fox jumps", 20) == "The quick brown fox..."
    assert string_utils.string_truncator("The  quick    brown    fox jumps", 20, True) == "The quick brown fox..."
    
def test_string_with_punctuation():
    """
    Test truncation of a string with punctuation.
    The string should be truncated to the specified max length,
    with an ellipsis appended if no word boundary is used.
    When word boundary is True, truncation should occur at the last
    word boundary before the max length.
    """

    assert string_utils.string_truncator("!Hello,worlds-how_are.you?", 10) == "!Hello,wor..."
    assert string_utils.string_truncator("!Hello,worlds-how_are.you?", 10, True) == "Hello..."
    
def test_string_with_punctuation_and_spaces():
    """
    Test truncation of a string with punctuation and spaces.
    The string should be truncated to the specified max length,
    with an ellipsis appended if no word boundary is used.
    When word boundary is True, truncation should occur at the last
    word boundary before the max length.
    """
    assert string_utils.string_truncator("!Hello,+ Sir_Tang@how-are.you?", 22) == "!Hello,+ Sir_Tang@how-..."
    assert string_utils.string_truncator("!Hello,+ Sir_Tang@how-are.you?", 22, True) == "Hello +..."
    
def test_string_with_apostrophes_and_hyphens():
    """
    Test truncation of a string with apostrophes and hyphens.
    The string should be truncated to the specified max length,
    with an ellipsis appended if no word boundary is used.
    When word boundary is True, truncation should occur at the last
    word boundary before the max length.
    """    
    assert string_utils.string_truncator("Don't state-of-the-art O'Connor", 50) == "Don't state-of-the-art O'Connor"
    assert string_utils.string_truncator("Don't state-of-the-art O'Connor", 50, True) == "Don't state-of-the-art O'Connor"

def test_string_with_only_separators():
    """
    Test truncation of a string with only separator characters.
    The string should be truncated to the specified max length,
    with an ellipsis appended if no word boundary is used.
    When word boundary is True, truncation should occur at the last
    word boundary before the max length.
    """
    assert string_utils.string_truncator("---'''--- -'-", 10) == "---'''---..."
    assert string_utils.string_truncator("---'''--- -'-", 10, True) == "---'''---..."
    
def test_empty_string():
    """
    Test truncation of an empty string.
    The string should not be modified when passed through the string_truncator.
    """
    assert string_utils.string_truncator("", 10) == ""
    assert string_utils.string_truncator("", 10, True) == ""
    
def test_string_exactly_at_max_length():
    """
    Test truncation of a string that is exactly at the max length.
    The string should not be modified when passed through the string_truncator.
    """
    test_str = "Hello World" #11 characters
    assert string_utils.string_truncator("Hello World", 11) == test_str
    assert string_utils.string_truncator("Hello World", 11, True) == test_str
    
def test_max_length_zero():
    """
    Test truncation of a string with a max length of zero.
    The string should only return an ellipsis.
    """
    assert string_utils.string_truncator("Hello, world!", 0) == "..."
    assert string_utils.string_truncator("Hello, world!", 0, True) == "..."

def test_unicode_characters():
    """
    Unicode characters test our handling of non-ASCII text.
    Each character might count differently in bytes vs length.
    """
    assert string_utils.string_truncator("Hello 世界", 7) == "Hello 世..."
    assert string_utils.string_truncator("Hello 世界", 7, True) == "Hello..."
    
def test_multiple_line_breaks():
    """
    Multiple line breaks test our handling of different types of whitespace.
    """
    assert string_utils.string_truncator("Hello\n\n\nWorld", 8, True) == "Hello..."
    assert string_utils.string_truncator("Hello\n\n\nWorld", 8) == "Hello Wo..."
    assert string_utils.string_truncator("Hello\r\n\tWorld", 8, True) == "Hello..."
    assert string_utils.string_truncator("Hello\r\n\tWorld", 8) == "Hello Wo..."

def test_word_exactly_at_boudary():
    """
    Tests what happens when a word ends exactly at max_length.
    Should we add ellipsis or not?
    """
    assert string_utils.string_truncator("Hello World", 5) == "Hello..."
    assert string_utils.string_truncator("Hello World", 5, True) == "Hello"
    
def test_long_word_with_internal_punctiuation():
    email = "very.long.email@example.com"
    assert string_utils.string_truncator("very.long.email@example.com", 15) == "very.long.email..."
    assert string_utils.string_truncator("very.long.email@example.com", 15, True) == "very long..."