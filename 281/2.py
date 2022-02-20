from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# attemp 1 WA 这个是要合并 相邻两个零之间的所有数字
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next
        prev = head
        while cur:
            if cur.val > 0:
                prev.next = cur
                prev = cur
            cur = cur.next
        prev.next = None
        return head.next

class Solution1:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag = False # flag为True表示已经处于一个group中了
        cur, _new = head.next, None
        prev = head
        while cur:
            if cur.val > 0:
                if not flag:
                    _new = ListNode(cur.val)
                    flag = True
                else:
                    _new.val += cur.val
            else:
                if flag:
                    prev.next = _new
                    prev = _new
                    flag = False
            cur = cur.next
        prev.next = None
        return head.next

def printListNode(_head):
    while _head:
        print(_head.val, end = " ")
        _head = _head.next
    print()

def transformList(_list):
    _head = ListNode(0, None)
    p = _head
    for x in _list:
        p.next = ListNode(x, None)
        p = p.next
    p.next = ListNode(0, None)
    return _head
    
def main():
    sol = Solution1()
    _input = transformList([0,3,1,0,4,5,2,0])
    _input1 = transformList([0,1,0,3,0,2,2,0])
    _output = sol.mergeNodes(_input)
    printListNode(_output)

if __name__ == '__main__':
    main()
