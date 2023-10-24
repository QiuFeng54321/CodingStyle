# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum=self.lti(l1)+self.lti(l2)
        list=self.itl(sum)
        print(sum)
        return list
        pass
    def lti(self,l: ListNode)-> int:
        ret=0
        dig=1
        buffer=l
        if(buffer==None):
            return 0
        while(True):
            ret+=buffer.val*dig
            if(buffer.next==None):
                break
            dig*=10
            buffer=buffer.next
        print(ret)
        return ret
    def itl(self,i: int)-> ListNode:
        copy=i
        l=[]
        '''current=ret
        last=ret
        while(copy!=0):
            digit=copy%10
            copy-=copy%10
            copy/=10
            last=current
            current.val=int(digit)
            current.next=ListNode(0)
            current=current.next
        last.next=None'''
        if(copy==0):
            return [0]
        for c in str(i):
            l.insert(0,int(c))
        return l