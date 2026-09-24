class node :
    def __init__(self , item = None,next = None):
        self.item  = item
        self.next = next
class Sll:
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
            self.start = n
    def insert_at_last(self,data):
        n = node(data)
        if self.is_empty():
            self.start = n
        else:
            if(self.start.next == None):
                self.start.next = n
            else:
                temp = self.start
                while temp.next!=None:
                    temp = temp.next
                temp.next = n
    def search(self,data):
        if self.start is None:
            return None
        else:
            temp = self.start
            while(temp!=None):
                if(temp.item == data):
                    return temp
                else:
                    temp = temp.next
            return None
    def insert_after(self,temp,data):
            n = node(data,temp.next)
            temp.next = n
    def print_item(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end = " ")
            temp = temp.next

    def size(self):
        count = 0
        temp = self.start
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    def delete_first(self):
        if self.start is None:
            return None
        else:
            if self.start.next is None:
                self.start = None
            else:
                self.start = self.start.next
    def delete_last(self):
        if self.start is None :
            return None
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next!=None:
                temp = temp.next
            temp.next = None

    def delete_item(self,data):
        if self.start is None:
            return None
        elif self.start.item == data and self.start.next == None:
            self.start = None
        else:
            temp = self.start
            if self.start.item == data:
                self.start = self.start.next
            else:
                while temp.next!=None:
                    if (temp.next.item == data):
                        temp.next = temp.next.next
                        break
                    temp = temp.next
    def delete_nth_from_last(self,n):
        num = 1
        temp = self.start
        if n == 1 and temp.next is None:
            self.start = None
        else:
            if (n == self.size()):
                self.start = temp.next
            else:
                while num<self.size()-n:
                    num+=1
                    temp = temp.next
                temp.next = temp.next.next              
    def size(self):
        count = 0
        temp = self.start

        while temp is not None:
            count += 1
            temp = temp.next
        return count
a = Sll()
a.insert_at_start(60)
a.insert_at_start(50)
a.insert_at_start(40)
a.insert_at_start(30)
a.insert_at_start(20)
a.insert_at_start(10)
a.insert_at_last(70)
a.print_item()
a.delete_nth_from_last(2)
print("\nSize:", a.size())