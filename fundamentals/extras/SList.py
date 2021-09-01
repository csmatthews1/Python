class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SNode(val)
        new_node.next = self.head
        self.head = new_node
        return self
    def print_values(self):
        curNode = self.head
        while(curNode != None):
            print(curNode.value)
            curNode = curNode.next
        return self
    def add_to_end(self, val):
        new_node = SNode(val)
        curNode = self.head
        if (self.head != None):
            while(curNode.next != None):
                curNode = curNode.next
            curNode.next = new_node
        else:
            self.head = new_node
        return self
    def remove_from_front(self):
        if (self.head != None):
            value = self.head.value
            self.head = self.head.next
            return value
        return None
    def remove_from_end(self):
        if(self.head != None):
            curNode = self.head
            while (curNode.next !=None):
                prevNode = curNode
                curNode = curNode.next
            prevNode.next = None
            return curNode.value
        return None
    def remove_val(self,val):
        curNode = self.head
        prevNode = None
        if (curNode != None):
            while (curNode.value != val):
                prevNode = curNode
                curNode = curNode.next
                if(curNode.next == None):
                    return False
            prevNode.next = curNode.next
            return True
        return False
    def insert_at(self, val, n):
        curNode = self.head;
        if (curNode != None):
            for x in range(n-1):
                if(curNode.next != None):
                    curNode = curNode.next
                else:
                    curNode.next = SNode(val)
                    return False;
            curNode.next = SNode(val)
            return True;
        else:
            self.head = SNode(val)
            return False;
class SNode:
    def __init__(self, val):
        self.value = val
        self.next = None

#Test add functions (front and end)
new_list = SList()
new_list.add_to_end(8).add_to_front(6).add_to_end(10).add_to_front(3).add_to_end(12)
new_list.print_values()

#Test removing from end
new_list.remove_from_end()
new_list.print_values()

#Test removing from front
new_list.remove_from_front()
new_list.print_values()

#Test removing by value
new_list.remove_val(8)
new_list.print_values()

