# main.py

from wordcount_tool.counter import WordCounter

# Create a sample text file to test with
with open("sample.txt", "w") as f:
    f.write("Hello world! This is a test. Hello world, again.")

# Create an object from our class blueprint
counter_obj = WordCounter("sample.txt")

# Call the new method to perform the counting
counts = counter_obj.count_words()

# Print the results
if counts:
    print("--- Word Counts ---")
    print(counts)