class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def Reverse_Node(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

linked_list = LinkedList(Node("Head", Node(1, Node(2, Node(3)))))
linked_list.Reverse_Node()
node = linked_list.head
while node:
    print(node.value)
    node = node.next

