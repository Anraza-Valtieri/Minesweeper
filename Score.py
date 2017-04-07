

counter = 0


class Node(object):
    def __init__(self, name, score, seed):
        # hold name,score,seed_data
        self.name = name
        self.score = score
        self.seed = seed
        self.next = None

    def getscore(self):
        return self.score

    def getAllInfo(self):
        alist = [self.name, str(self.score), self.seed]
        print alist
        return alist


class Stack(object):
    def __init__(self):
        # self.top = -1
        self.data = []

    def isEmpty(self):
        return self.data == []

    def push(self, value):
        self.data.append(value)
        # self.top += 1
        # self.data[self.top] = value

    def pop(self):
        if (len(self.data) > 0):
            return self.data.pop()
        else:
            print("Stack is empty.")

    def peek(self):
        return self.data[len(self.data) - 1]

    def printStack(self):
        for data in reversed(self.data):
            print data


class LinkedList(object):
    head = None

    # methods to insert,delete,search

    def insert(self, name, score, seed):
        global counter
        # insert  values into node
        current = self.head
        i = 0

        if current is None:
            # if there is no node, current node becomes head
            node = Node(name, score, seed)
            node.next = None
            self.head = node
            counter += 1
            return
        if current.score < score:
            node = Node(name, score, seed)
            node.score = score
            node.next = current
            self.head = node
            counter += 1
            return

        while current.next is not None:
            if current.next.score < score:
                break
            current = current.next
        node = Node(name, score, seed)
        node.score = score
        node.next = current.next
        current.next = node
        counter += 1

        while counter > 100:
            # delete head that is more than 100
            temp = self.head
            self.head = temp.next
            current = self.head
            counter -= 1

        return

    def printList(self):  #
        i = 1
        print("Current list content:")
        temp = self.head
        scoresStack = Stack()

        while temp is not None:
            print("Node:", i)  # this is to show iteration
            # temp.getAllInfo()#'[',temp.name,',',temp.score,',',temp.seed,']\n',

            print scoresStack.isEmpty()  # can be remove, used to check if stack is empty
            scoresStack.push(temp.getAllInfo())

            print "-----------------------------------"

            scoresStack.printStack()  # can be remove too

            temp = temp.next
            i += 1
        return scoresStack  # Return the stack as a list

    def returnValList(self):

        temp = self.head

        while temp is not None:
            return temp.getAllInfo()
            temp = temp.next


newll = LinkedList()

