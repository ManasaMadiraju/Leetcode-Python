# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt
        return prev


def main():
    head = [1,2,3,4,5]
    s=Solution()
    result=s.reverseList(head)
    print(result)

if __name__ == "__main__":
    main()
    