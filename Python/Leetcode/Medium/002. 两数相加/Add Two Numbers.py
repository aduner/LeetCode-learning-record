# Link：https://leetcode-cn.com/problems/add-two-numbers/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def dfs(l, r, i):
            if not l and not r and not i:
                return None
            s = (l.val if l else 0) + (r.val if r else 0) + i
            node = ListNode(s % 10)
            node.next = dfs(l.next if l else None,
                            r.next if r else None, s // 10)
            return node
        return dfs(l1, l2, 0)
