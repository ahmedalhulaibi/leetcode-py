def make_exports(completed: bool) -> dict[str, object]:
    class Solution:
        def two_sum(self, nums: list[int], target: int) -> list[int]:
            if not completed:
                raise NotImplementedError
            seen: dict[int, int] = {}
            for index, number in enumerate(nums):
                complement = target - number
                if complement in seen:
                    return [seen[complement], index]
                seen[number] = index
            raise ValueError("No valid pair")

    return {"Solution": Solution}
