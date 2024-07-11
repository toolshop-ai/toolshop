class DoublyLinkedListNode:
    next: 'DoublyLinkedListNode' = None
    prev: 'DoublyLinkedListNode' = None

    def insert_after(self, that: 'DoublyLinkedListNode'):
        that.next = self.next
        that.prev = self
        self.next.prev = that
        self.next = that
