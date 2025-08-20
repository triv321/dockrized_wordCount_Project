# tests/test_counter.py

from wordcount_tool.counter import WordCounter
import os

# A test function must start with the word 'test_'
def test_word_counting():
    """
    Tests the basic word counting functionality on a simple sentence.
    """
    # 1. Setup: Create a temporary file with known content.
    filepath = "test_file.txt"
    with open(filepath, "w") as f:
        f.write("hello world hello")

    # 2. Execution: Run the code we are testing.
    counter = WordCounter(filepath)
    counts = counter.count_words()

    # 3. Assertion: Check if the result is what we expect.
    assert counts["hello"] == 2
    assert counts["world"] == 1

    # 4. Teardown: Clean up the temporary file.
    os.remove(filepath)


def test_file_not_found():
    """
    Tests that the method correctly returns None when the file does not exist.
    """
    # 1. Setup
    counter = WordCounter("non_existent_file.txt")

    # 2. Execution
    result = counter.count_words()

    # 3. Assertion
    assert result is None