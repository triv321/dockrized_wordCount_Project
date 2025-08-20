# wordcount_tool/counter.py
import re # We need to import the regular expression module

class WordCounter:
    """A simple class to count words in a text file."""

    def __init__(self, filepath):
        """Initializes the WordCounter with the path to a file."""
        self.filepath = filepath
        self.word_counts = {}  # A dictionary to store word counts
        print(f"WordCounter object initialized for file: {self.filepath}")

    def count_words(self):
        """Reads the file and counts the occurrences of each word."""
        try:
            with open(self.filepath, 'r') as f:
                text = f.read()

                # --- Text Cleaning ---
                # Convert to lowercase
                text = text.lower()
                # Remove punctuation using a regular expression
                text = re.sub(r'[^\w\s]', '', text)

                # Split the text into a list of words
                words = text.split()

                # Count the words
                for word in words:
                    self.word_counts[word] = self.word_counts.get(word, 0) + 1
            
            print("Word counting complete.")
            return self.word_counts

        except FileNotFoundError:
            print(f"Error: The file at {self.filepath} was not found.")
            return None