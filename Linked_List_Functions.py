class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def remove_dup(self):
        prev = None
        curr = self.head
        dic = {}
        while curr:
            if curr.data in dic:
                prev.next = curr.next
                curr = None

            else:
                dic[curr.data] = 1
                prev = curr
            curr = prev.next
        return self.head

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def show_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def len_of_list(self):
        count = 0
        curr = self.head
        while curr:
            count = count + 1
            curr = curr.next
        return count

    def nth_to_last(self,n):
        #method 1
        # count = LinkedList.len_of_list(self)
        # curr = self.head
        # while curr:
        #     if count==n:
        #         print(curr.data)
        #         return
        #     count -=1
        #     curr = curr.next
        # if curr == None:
        #     print('out of bounds')
        #method2
        p = self.head
        q = self.head

        count =0
        while q and count<n:
            q = q.next
            count +=1
        if not q:
            print("str(n) is greater than length of string")
            return

        while p and q:
            p = p.next
            q = q.next
        return p.data

    def rotate_llist(self,k):
        p = self.head
        q = self.head
        prev = None

        count = 0
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count +=1
        p = prev

        while q:
            prev = q
            q = q.next
        q = prev

        q.next =self.head
        self.head = p.next
        p.next = None

    def palindrome_llist(self):
        s =''
        p = self.head
        while p:
            s += p.data
            p =p.next

        return s == s[::-1]

    def tail_to_head(self):
        prev = None
        curr = self.head
        while curr.next:
            prev = curr
            curr = curr.next
        curr.next = self.head
        prev.next = None
        self.head = curr

    def sum_lists(self,llist2):
        p =self.head
        q =llist2.head
        carry = 0
        sum_list = LinkedList()

        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data

            sumi = i + j + carry
            if sumi>=10:
                carry = 1
                s = sumi%10
                sum_list.append(s)
            else:
                carry = 0
                sum_list.append(sumi)

            if p:
                p = p.next

            if q:
                q = q.next

        sum_list.show_list()









llist1 = LinkedList()
llist1.append(1)
llist1.append(2)
llist1.append(3)
llist2 = LinkedList()
llist2.append(4)
llist2.append(2)
# llist.show_list()
# print("\n")
# llist.tail_to_head()
# llist.show_list()
# # print(llist.len_of_list())
# # print(llist.nth_to_last(2))
# print("\n")
# llist.rotate_llist(4)
# llist.show_list()
llist1.sum_lists(llist2)












