class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def Delete_Node_value(self, value):
        dummy = Node(0, self.head)
        prev = dummy
        while prev.next:
            if prev.next.value == value:
                prev.next = prev.next.next
            else:
                prev = prev.next
        self.head = dummy.next

linked_list = LinkedList(Node("Head", Node(1, Node(2, Node(1, Node(3, Node(2)))))))
linked_list.Delete_Node_value(1)
linked_list.Delete_Node_value(2)
node = linked_list.head
while node:
    print(node.value)
    node = node.next
