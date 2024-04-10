# Remove the empty lines from a String in Python

import os


multiline_string = """\
First line

Second line

Third line


"""


without_empty_lines = os.linesep.join(
    [
        line for line in multiline_string.splitlines()
        if line
    ]
)

# First line
# Second line
# Third line
print(without_empty_lines)