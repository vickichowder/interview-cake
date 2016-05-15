class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


def delete_node(node):
    if node.next is None:
        node.value = None
    else:
        next_node = node.next
        try:
            node.value = next_node.value
            node.next = next_node.next
        except Exception as e:
            raise('Exception encountered:', e)

def print_list(node, linked_list):
    if (node.value != None):
        linked_list += node.value
    if (node.next != None):
        print_list(node.next, linked_list)
    else:
        print(linked_list)

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

print_list(a, [])
delete_node(c)
print_list(a, [])
