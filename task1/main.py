class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def sorted_insert(self, sorted_list, new_node):
        if not sorted_list or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            return new_node
        else:
            current = sorted_list
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            return sorted_list

    def merge_sorted_lists(self, list2):
        """Об'єднання двох відсортованих списків."""
        dummy = Node()
        tail = dummy
        l1, l2 = self.head, list2.head
        while l1 and l2:
            if l1.data < l2.data:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        merged_list = LinkedList()
        merged_list.head = dummy.next

        return merged_list

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)


# Створення і тестування функцій однозв'язного списку
if __name__ == "__main__":
    # Тест реверсування списку
    list1 = LinkedList()
    for i in range(1, 6):
        list1.append(i)
    print("Оригінальний список:", list1)
    list1.reverse()
    print("Реверсований список:", list1)

    # Тест сортування вставками
    list2 = LinkedList()
    list2.append(3)
    list2.append(1)
    list2.append(5)
    list2.append(2)
    list2.append(4)
    print("\nНе відсортований список:", list2)
    list2.insertion_sort()
    print("Відсортований список:", list2)

    # Тест об'єднання відсортованих списків
    list3 = LinkedList()
    list3.append(1)
    list3.append(3)
    list3.append(5)
    list4 = LinkedList()
    list4.append(2)
    list4.append(4)
    list4.append(6)
    merged_list = list3.merge_sorted_lists(list4)
    print("\nОб'єднаний відсортований список:", merged_list)
