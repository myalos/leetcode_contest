# 22 - 5 - 1 重做了一遍
from typing import *

class Solution:
    def mergeNodes(self, head : Optional[ListNode]) -> Optional[ListNode]:
        # 用两个指针来遍历每一组的数据
        _head, _tail = head, head
        ans = ListNode(0) # 头指针
        p = ans
        while _head and _tail.next:
            # 每一次循环之后_head和_tail指向同一个位置，所以当_tail.next 为None的时候就不需要再执行了
            while _tail.next:  # 定位到下一组的位置
                _tail = _tail.next
                if _tail.val == 0:
                    break
            t = 0 # 一组的数据的和
            _head = _head.next
            while id(_head) != id(_tail):
                t += _head.val
                _head = _head.next
            p.next = ListNode(t)
            p = p.next
        return ans.next
# 时间2456ms 击败23.80%

# 最快的方法是1452ms 这个方法没有添加新的ListNode

class Solution:
    def mergeNodes(self, head : Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        ne = cur.next
        s = 0
        while ne:
            if s == 0:
                # 每组的开始 将cur往后移动一格
                cur = cur.next
            if ne.val == 0:
                cur.val = s
                s = 0
            else:
                s += ne.val
            ne = ne.next
        cur.next = None
        return cur.next
