class Node:
    def __init__(self, data):
        self.data = data
        self.nextval = None


class linked_list:
    def __init__(self):
        self.head = None
        self.size=0

    def add_to_end(self, data):
        node=Node(data)
        print(self.size)
        if(self.size==0):
            self.head=node
            self.size+=1
            return 0
        current_node=self.head
        while(True):
            if(current_node.nextval is None):
                current_node.nextval=node
                break
            current_node=current_node.nextval
            self.size+=1
        
    
    def add_to_start(self,data):
        node=Node(data)
        node.nextval=self.head
        self.head=node
        self.size+=1

    def add_to_loc(self,data,loc):
        node=Node(data)
        current_node=self.head
        if(self.size<loc-1):
            print('Can not perform this operation')
            return 0
        elif(loc==1):
            node.nextval=self.head
            self.head=node
            return 0
        for i in range(loc-2):
            current_node=current_node.nextval
        node.nextval=current_node.nextval
        current_node.nextval=node
        self.size+=1

    def delete_end(self):
        current_node=self.head
        if(self.size==1):
            self.head=None
            self.size-=1
            return 0
        elif(self.size==0):
            print('Linked List is Empty')
            return 0
        while(current_node.nextval.nextval is not None):
            current_node=current_node.nextval
        current_node.nextval=None
        self.size-=1
        
    def delete_start(self):
        current_node=self.head
        if(self.size==1):
            self.head=None
            self.size-=1
            return 0
        elif(self.size==0):
            print('Linked List is Empty')
            return 0
        self.head=self.head.nextval
        self.size-=1

    def delete_loc(self,loc):
        if(self.size<loc):
            print('Can not perform this operation')
            return 0
        elif(self.size==1):
            self.head=None
            self.size-=1
            return 0
        elif(self.size==0):
            print('Linked List is empty')
            return 0
        current_node=self.head
        for i in range(loc-2):
            current_node=current_node.nextval
        temp=current_node.nextval
        current_node.nextval=current_node.nextval.nextval
        temp.nextval=None
        self.size-=1

    def traverse_ll(self):
        if(self.size==0):
            print('Linked List is Empty')
            return 0
        currrent_node=self.head
        while(currrent_node is not None):
            print(currrent_node.data)
            currrent_node=currrent_node.nextval
        


def create_sll(node):
    sll=linked_list()
    sll.head=node
    sll.size+=1
    return sll
    


fn=int(input('Enter 1st node data: '))
nll=create_sll(Node(fn))
while(True):
    choice=int(input(' 1-Traverse \n 2-add to end \n 3-add to start \n 4-add to location \n 5-delete end \n 6-delete start \n 7-delete at location \n 8-exit \n Enter the choice: ',))
    if(choice==1):
        nll.traverse_ll()
    elif(choice==2):
        data=int(input('Enter the node data: '))
        nll.add_to_end(data)
    elif(choice==3):
        data=int(input('Enter the node data: '))
        nll.add_to_start(data)
    elif(choice==4):
        data=int(input('Enter the node data: '))
        loc=int(input('Enter the location: '))
        nll.add_to_loc(data,loc)
    elif(choice==5):
        nll.delete_end()
    elif(choice==6):
        nll.delete_start()
    elif(choice==7):
        loc=int(input('Enter the location: '))
        nll.delete_loc(loc)
    elif(choice==8):
        exit(0)
    else:
        print('Wrong Input')
        exit(0)
        

