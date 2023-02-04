class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def Delete_Dupl_Node(self):
        current = self.head
        values = set()
        prev = None
        while current:
            if current.value in values:
                prev.next = current.next
            else:
                values.add(current.value)
                prev = current
            current = current.next

linked_list = LinkedList(Node("Head", Node(1, Node(2, Node(1, Node(3, Node(2)))))))
linked_list.Delete_Dupl_Node()
node = linked_list.head
while node:
    print(node.value)
    node = node.next
