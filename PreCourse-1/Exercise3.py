#  Implement Singly Linked List.
class ListNode:
    """
    A node in a singly-linked list.
    """

    def __init__(self, data=None, next=None):
        self.data=data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        newNode = ListNode(data)
        if self.head is None:
            self.head=newNode
            return
        cur = self.head
        while cur.next:
            cur=cur.next
        cur.next = newNode


    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        cur = self.head
        while cur:
            if key==cur.data:
                return cur.data
            cur=cur.next
        return None

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        if self.head and key == self.head.data:
            self.head=self.head.next
            return
        prev, cur = self.head, self.head.next
        while cur:
            if cur.data==key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
        return 'Key not found'

    def print(self):
        cur = self.head
        while cur:
            print(cur.data,end='->')
            cur = cur.next


ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.print()
print(ll.find(2))
ll.print()
print(ll.remove(2))
ll.print()
