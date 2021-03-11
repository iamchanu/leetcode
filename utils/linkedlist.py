# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_linked_list(l):
    if l:
        return ListNode(val=l[0], next=to_linked_list(l[1:]))
    else:
        return None

def from_linked_list(ll):
    if ll is not None:
        return [ll.val] + from_linked_list(ll.next)
    else:
        return []

def print_node(node):
    if node: 
        return node.val
    else:
        return None
