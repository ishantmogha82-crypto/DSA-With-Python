class node:
    def __init__(self,prev = None,item = None,next = None):
        self.prev = prev
        self.item= item
        self.next = next
class DLL:
    def __init__(self,start = None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n = node(data)
        if self.is_empty():
            self.start = n
        else:
            n.next = self.start
            self.start.prev = n
            self.start = n
    def insert_at_last(self,data):
        n = node(data)
        if self.start is None:
            self.start = n
        else :
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n.prev = temp
            temp.next = n
    def search(self,data):
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return temp
                temp = temp.next
            return None
    def insert_after(self,temp,data):
        if temp is None:
            return None
        n = node(data)
        if temp.next is None:
            n.prev = temp
            temp.next = n
        else:
            n.prev = temp
            n.next = temp.next
            temp.next.prev = n
            temp.next = n
    def print_item(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end = " ")
            temp = temp.next



            