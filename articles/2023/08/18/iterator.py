
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next: "Node" | None = None # not a best solution but there is no import :)


class LinkedList:
    def __init__(self, head, *other_nodes) -> None:
        self.head = head
        if other_nodes:
            head.next = other_nodes[0]
        for i, node in enumerate(other_nodes):
            if (i + 1) < len(other_nodes):
                node.next = other_nodes[i + 1]
        self.current = None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is not None:
            val = self.current.val
            self.current = self.current.next
            return val
        raise StopIteration


def show_iterator():
    from os.path import basename

    print()
    print(f"{basename(__file__):_^80}")

    node1 = Node(1)
    node2 = Node(2)

    my_list = LinkedList(node1, node2)

    for n in my_list:
        print(n)

    my_list2 = LinkedList(Node(4))
    for n in my_list2:
        print(n)

    my_list3 = LinkedList(Node(1), Node(2), Node(3), Node(4), Node(5))
    for n in my_list3:
        print(n)
