class Solution:
    def splitListToParts(self, head, k):
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        size = length // k
        extra = length % k
        ans = []
        curr = head
        for i in range(k):
            part_size = size
            if extra > 0:
                part_size += 1
                extra -= 1
            if part_size == 0:
                ans.append(None)
                continue
            part_head = curr
            for j in range(part_size - 1):
                curr = curr.next
            next_part = curr.next
            curr.next = None
            ans.append(part_head)
            curr = next_part
        return ans