from leetcode_py import ListNode


def make_exports(completed: bool) -> dict[str, object]:
    class Solution:
        def reverse_list(self, head: ListNode[int] | None) -> ListNode[int] | None:
            if not completed:
                raise NotImplementedError
            previous = None
            while head is not None:
                following = head.next
                head.next = previous
                previous = head
                head = following
            return previous

    return {"Solution": Solution}
