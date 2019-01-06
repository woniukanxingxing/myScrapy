class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_sore(self):
        print('%s:%s' % (self.name, self.score))


Student('luxi',99).print_sore()



