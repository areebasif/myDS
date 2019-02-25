class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def show_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def prepend(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self,prev_node, data):
        if not prev_node:
            print("previous node not in the list")
        new_node = node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self,key):
        current_node=self.head
        if current_node and current_node.data ==key:
            self.head = current_node.next
            current_node.next = None
            return
        prev = None
        while current_node and current_node.data !=key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None

    def delete_position(self,idx):
        current_node = self.head

        if idx == 0:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        count = 1
        while current_node and count!= idx:
            prev = current_node
            current_node = current_node.next
            count = count + 1

        if current_node is None:
            return

        # prev.next = current_node.next
        current_node = None








llist = linked_list()
llist.append('A')
llist.append('B')

llist.prepend('E')

llist.insert_after(llist.head.next,'C')
llist.show_list()
llist.delete_node('C')

llist.delete_position(1)
llist.show_list()

