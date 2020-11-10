class Something:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.name


class Something_list:
    def __init__(self, name):
        self.first = Something(name)
        self.last = self.first
        self.current = self.first

    def add(self, name):
        self.last.next = Something(name)
        self.last = self.last.next

    def get_last(self):
        print(self.last)
        self.current = self.first
        while self.current.next != self.last:
            self.last.prev = self.current.next
            self.current = self.current.next
        self.last = self.last.prev

    def get_first(self):
        print(self.first)
        self.first = self.first.next


figure = Something_list(input())
figure.add(input())
figure.add(input())
figure.add(input())
figure.add(input())
figure.add(input())
figure.add(input())
figure.add(input())
figure.get_first()
figure.get_last()
figure.get_first()
figure.get_last()
figure.get_first()
figure.get_last()
figure.get_last()