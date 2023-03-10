# head = {
    # "value": 11,
    # "next": {
            # "value":3,
            # "next": {
                    # "value": 23,
                    # "next": {
                            # "value": 7,
                            # "next": None
    
                            # }
                    # }

            # }
    # }


# print(head["next"]['next']['value'])

# print(my_linked_list.head.next.next.value)


# class Node:
    # def __init__(self, value):
        # self.value = value
        # self.next = None
 


# class LinkedList:
    # def __init__(self, value):
        # new_node = Node(value)
        # self.head = new_node
        # self.tail = new_node
        # self.length = 1


# my_linked_list = LinkedList(4)   
# print(my_linked_list.head.value)     




# def print_list(self):
    # temp = self.head
    # while temp is not None:
        # print(temp.value)
        # temp = temp.next



# class Node:
    # def __init__(self, value):
        # self.value = value
        # self.next = None

# class LinkedList:
    # def __init__(self, value):
        # new_node = Node(value)
        # self.head = new_node
        # self.tail = new_node
        # self.length = 1

# my_linked_list = LinkedList(4)
# print(my_linked_list.head.value)   





##                                              ###LINKED LIST PROGRAM FOR APPENDING 


class Node:
     def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value) 
            temp = temp.next               



    def append(self, value):
        new_node = Node(value)
        if self.length== 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node  
            self.tail = new_node  

        self.length += 1    
        return True
    


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()   




######                                                 LINKEDLIST PROGRAM FOR POPPING ##########



def pop(self):
    if self.length == 0:
        return None


    temp = self.head
    pre = self.head



    while(temp.next):
        pre = temp
        temp = temp.next

    self.tail = pre
    self.tail.next = None
    self.length -=1

    if self.length == 0:
        self.head = None
        self.tail = None
    return temp    

my_linked_list = LinkedList(1)
my_linked_list.print_list()    

# print(my_linked_list.pop()

print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())




def prepend(self,value):
    new_node = Node(value)
    if self.length == 0:
        self.head = new_node
        self.tail = new_node

    else:
        new_node.next = self.head
        self.head = new_node

    self.length +=1
    return True

my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.prepend(1)
my_linked_list.print_list()        
    




def pop_first(self):
    if self.length == 0:

        