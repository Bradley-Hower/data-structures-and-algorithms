from linked_list_pack.linked_list import LinkedList, Node

def zip_lists(list1, list2):
    zipped_list = LinkedList()

    current1 = list1.head
    current2 = list2.head

    while current1 or current2:
        # Append a node from list1 to the zipped list
        if current1 is not None:
            zipped_list.append(current1.value)
            current1 = current1.next

        # Append a node from list2 to the zipped list
        if current2 is not None:
            zipped_list.append(current2.value)
            current2 = current2.next

    return zipped_list
