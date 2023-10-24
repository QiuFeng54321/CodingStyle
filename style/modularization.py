
import random


class Node:
    def __init__(self, value, next = -1) -> None:
        self.Value = value
        self.Next = next


HeadPointer = -1
FreePointer = 0
LList = [Node(None, i + 1) for i in range(100)]
LList[-1].Next = -1


def InsertAtHead(val):
    global HeadPointer, FreePointer, LList
    if FreePointer == -1: raise Exception("Capacity full")
    newNode = FreePointer
    FreePointer = LList[FreePointer].Next
    LList[newNode].Value = val
    LList[newNode].Next = HeadPointer
    HeadPointer = newNode
    
def DeleteHead():
    global HeadPointer, FreePointer, LList
    if HeadPointer == -1: raise Exception("Cannot delete nodes when the list is empty")
    newHead = LList[HeadPointer].Next
    val = LList[HeadPointer].Value
    LList[HeadPointer].Next = FreePointer
    FreePointer = HeadPointer
    HeadPointer = newHead
    return val
def Insert(idx, val):
    global HeadPointer, FreePointer, LList
    if idx == 0: return InsertAtHead(val)
    cur = HeadPointer
    prev = -1
    for i in range(idx):
        prev = cur
        cur = LList[cur].Next
        if prev == -1: raise IndexError()
    if FreePointer == -1: raise MemoryError()
    newNode = FreePointer
    FreePointer = LList[FreePointer].Next
    LList[newNode].Next = cur
    LList[newNode].Value = val
    LList[prev].Next = newNode
def InsertAtEnd(val):
    global HeadPointer, FreePointer, LList
    if FreePointer == -1: raise Exception("Memory full")
    cur = HeadPointer
    while cur != -1 and LList[cur].Next != -1:
        cur = LList[cur].Next
    newNode = FreePointer
    FreePointer = LList[FreePointer].Next
    LList[newNode].Value = val
    LList[newNode].Next = -1
    if cur == -1:
        HeadPointer = newNode
    else:
        LList[cur].Next = newNode
def Delete(val):
    """Finds the node with the value while keeping track of the previous node, then
    detach the node found

    :param val: Value to delete
    :type val: any
    :return: Whether the node is found
    :rtype: bool
    """
    
    global HeadPointer, FreePointer, LList
    cur = HeadPointer
    prev = -1
    while cur != -1 and LList[cur].Value != val:
        prev = cur
        cur = LList[cur].Next
    if cur == -1: return False
    if LList[cur].Value != val: return False
    if prev == -1:
        HeadPointer = LList[HeadPointer].Next
    else:
        LList[prev].Next = LList[cur].Next
    LList[cur].Next = FreePointer
    FreePointer = cur
    return True
def DeleteAt(idx):
    global HeadPointer, FreePointer, LList
    if idx == 0:
        newHead = LList[HeadPointer].Next
        LList[HeadPointer].Next = FreePointer
        FreePointer = HeadPointer
        HeadPointer = newHead
        return LList[HeadPointer].Value
    cur = HeadPointer
    prev = -1
    for i in range(idx):
        prev = cur
        cur = LList[cur].Next
        if prev == -1: raise IndexError()
    LList[prev].Next = LList[cur].Next
    LList[cur].Next = FreePointer
    FreePointer = cur
    return LList[cur].Value

def DeleteAtEnd():
    global HeadPointer, FreePointer, LList
    if HeadPointer == -1: raise Exception("List empty")
    cur = HeadPointer
    prev = -1
    while cur != -1 and LList[cur].Next != -1:
        prev = cur
        cur = LList[cur].Next
    if prev == -1:
        HeadPointer = LList[HeadPointer].Next
    else:
        LList[prev].Next = LList[cur].Next
    LList[cur].Next = FreePointer
    FreePointer = cur
    return LList[cur].Value

def Search(val):
    global HeadPointer, FreePointer, LList
    cur = HeadPointer
    i = 0
    while cur != -1 and LList[cur].Value != val:
        i += 1
        cur = LList[cur].Next
    if cur == -1: return -1
    return i

def InsertIntoSorted(val):
    global HeadPointer, FreePointer, LList
    cur = HeadPointer
    prev = -1
    while cur != -1 and LList[cur].Value < val:
        prev = cur
        cur = LList[cur].Next
    newNode = FreePointer
    FreePointer = LList[FreePointer].Next
    LList[newNode].Next = cur
    LList[newNode].Value = val
    if prev != -1:
        LList[prev].Next = newNode
    else:
        HeadPointer = newNode
    
def PrintItems():
    global HeadPointer, FreePointer, LList
    cur = HeadPointer
    res = "["
    while cur != -1:
        res += str(LList[cur].Value)
        if LList[cur].Next != -1: res += ", "
        cur = LList[cur].Next
    res += "]"
    print(res)

# InsertAtEnd(1)
# InsertAtEnd(2)
# InsertAtEnd(3)
# InsertAtEnd(4)
# PrintItems()
# InsertIntoSorted(5)
# InsertIntoSorted(0)
# PrintItems()
# Delete(2)
# PrintItems()
# Delete(1)
# PrintItems()
# Delete(4)
# PrintItems()
# Delete(3)
# PrintItems()
# # Delete(2)
# InsertAtEnd(1)
# InsertAtEnd(2)
# InsertAtEnd(3)
# InsertAtEnd(4)
# InsertAtHead(0)
# PrintItems()
# DeleteAtEnd()
# DeleteAtEnd()
# DeleteAtEnd()
# DeleteAtEnd()
# # DeleteAtEnd()
# PrintItems()
# DeleteAt(0)
# PrintItems()
# print(Search(0))
# print(Search(5))
# print(Search(500))

if __name__ =="__main__":
    # test add at head
    print("-"*20,"test addAtHead","-"*20)
    items = [i for i in range(11)] # 0,1,2...10
    for item in items:
       InsertAtHead(item)
    PrintItems()
    print()
    print("-" * 20, "test popAtHead", "-" * 20)
    for i in range(11):
        item = DeleteAtEnd()
        print(item, end = " ")
    print()

    print("-" * 20, "test addAtTail", "-" * 20)
    for item in items:
        InsertAtEnd(item)
    PrintItems()
    print()

    print("-" * 20, "test popAttail", "-" * 20)
    for i in range(11):
        item = DeleteAtEnd()
        print(item, end = " ")
    print()

    print("-" * 20, "test popItem", "-" * 20)
    for item in items:
        InsertAtEnd(item)
    PrintItems()
    print()
    popItemCases= [ 0,3,9,11]
    for item in popItemCases:
        if Delete(item):
            print(f"pop  {item} ...... successful!")
        else:
            print(f"pop  {item} ...... fail!")
    PrintItems()

    # left 1,3,4,5,6,7,8
    print("-" * 20, "test searchList", "-" * 20)
    testcases=[1,4,8,9]  # predict result should be success, success, success, fail
    for case in testcases:
        if Search(case) != -1:
            print(f"I find {case}. success ... ...")
        else:
            print(f"I could not find {case}. fail... ...")

    print("-" * 20, "test insertToOrderedList", "-" * 20)
    for i in range(7):
        DeleteAtEnd()
    print("show empty list")
    PrintItems()
    print("#############")
    testcases = [random.randint(1,100) for i in range(10)]
    print(testcases)
    for case in testcases:
        InsertIntoSorted(case)
    PrintItems()
