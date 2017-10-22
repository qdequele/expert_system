import sys

class Error:

    def __init__(self, message):
        print(message)
        sys.exit(1)
