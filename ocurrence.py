
class Ocurrence:
    def __init__(self, filename, word, ocurrences):
        self.filename = filename
        self.word = word
        self.ocurrences = ocurrences

    def __repr__(self):
        return "<Ocurrence filename:%s word:%s ocurrences:%d>" % (self.filename, self.word, self.ocurrences)

    def __str__(self):
        return self.filename + ": " + self.word + " " + "(" + str(self.ocurrences) + " ocurrences" + ")"
