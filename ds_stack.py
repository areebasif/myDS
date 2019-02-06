class stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        print(self.items)

    def is_empty(self):
        return self.items == []

    def top_item(self):
        if not self.is_empty():
            return self.items[-1]


s = stack()
s.push('a')
s.push('b')
s.push('c')
s.push('d')

s.get_stack()
print(s.is_empty())
print(s.top_item())