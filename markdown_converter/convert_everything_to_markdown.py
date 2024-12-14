from markitdown import MarkItDown
import sys

markitdown = MarkItDown()

# get first argument from command line
file_path = sys.argv[1]

# check if file exists
try:
    with open(file_path):
        result = markitdown.convert(file_path)

        print(result.text_content)

except FileNotFoundError:
    print("File not found")
