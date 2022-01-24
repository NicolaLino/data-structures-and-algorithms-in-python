class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_begining(self, data):
        self.head = Node(data, self.head)

    def print(self):
        if self.head == None:
            print("The LinkedList Is Empty")
            return

        itr = self.head
        string = ''
        while itr:
            string += str(itr.data) + '=>'
            itr = itr.next

        print(string)

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            itr = itr.next
            counter += 1
        return counter

    def insert_at(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index, \n try again")

        if index == 0:
            self.insert_at_begining(data)
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data, itr.next)
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if index-1 == count:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_values(self, data_list):
        self.head = None
        for item in data_list:
            self.insert_at_end(item)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head == None:
            return
        if self.head.next == data:
            self.head = self.head.next

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break

            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

    # ll.insert_values([45,7,12,567,99])
    # ll.insert_at_end(67)
    # ll.print()
