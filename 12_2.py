class Line:
    def __init__(self):
        self.line = []

    def add(self, name):
        self.line.append(name)

    def getLast(self):
        last_name = self.line[len(self.line)-1]
        print(last_name)
        self.line.pop(len(self.line)-1)

    def getFirst(self):
        first_name = self.line[0]
        print(first_name)
        self.line.pop(0)


a = Line()
a.add('кот')
a.add('слон')
a.add('тигр')
a.add('жираф')
a.add('собака')
a.add('лось')
a.getFirst()
a.getLast()
a.getFirst()
a.getLast()