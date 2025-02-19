import pytest
import inspect
from assignment import (
    create_and_read_file,
    write_user_info,
    count_words_in_file,
    find_longest_word_in_file
)

@pytest.mark.parametrize("filename, content", [
    ("test_story.txt", "Once upon a time in a faraway land."),
    ("test_story2.txt", "Python is a powerful programming language."),
])
def test1(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    
    assert create_and_read_file(filename) is None  # Assuming it prints content but returns nothing

@pytest.mark.parametrize("filename, name, age", [
    ("test_user1.txt", "Alice", 25),
    ("test_user2.txt", "Bob", 30),
])
def test2(filename, name, age):
    write_user_info(filename, name, age)
    
    with open(filename, "r") as f:
        content = f.read().strip()
    
    assert content == f"name: {name}, age: {age}" or content == f"Name: {name}, Age: {age}"

@pytest.mark.parametrize("filename, content, expected_count", [
    ("test_words.txt", "Hello world!", 2),
    ("test_words2.txt", "This is a test file with multiple words.", 8),
    ("empty.txt", "", 0)
])
def test3(filename, content, expected_count):
    with open(filename, "w") as f:
        f.write(content)
    
    assert count_words_in_file(filename) == expected_count

@pytest.mark.parametrize("filename, content, expected_word", [
    ("test_longest.txt", "Find the longest word in this file.", "longest"),
    ("test_longest2.txt", "Short words only.", "Short"),
    ("empty.txt", "", "")
])
def test4(filename, content, expected_word):
    with open(filename, "w") as f:
        f.write(content)
    
    assert find_longest_word_in_file(filename) == expected_word
