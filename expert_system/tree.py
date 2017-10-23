class Tree:

    tree = {}

    def __init__(self):
        pass

    def add(self, letter, fact):
        if letter is not in tree:
            tree[letter] = fact
            return True
        return False

    def get(self, letter)
        return tree[letter]
