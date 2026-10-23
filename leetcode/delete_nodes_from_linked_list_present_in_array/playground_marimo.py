# /// script
# requires-python = ">=3.10"
# dependencies = ["marimo==0.25.2", "leetcode-py-sdk[practice]==0.0.0"]
# [tool.uv.sources]
# leetcode-py-sdk = { path = "../..", editable = true }
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from leetcode_py.practice import run_practice_tests

    return mo, run_practice_tests


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # 3217. Delete Nodes From Linked List Present in Array

    **Medium** · Array, Hash Table, Linked List

    You are given an array of integers `nums` and the `head` of a linked list. Return the `head` of the modified linked list after <strong>removing</strong> all nodes from the linked list that have a value that exists in `nums`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample0.png)

    ```
    Input: nums = [1,2,3], head = [1,2,3,4,5]
    Output: [4,5]
    Explanation: Remove the nodes with values 1, 2, and 3.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample1.png)

    ```
    Input: nums = [1], head = [1,2,1,2,1,2]
    Output: [2,2,2]
    Explanation: Remove the nodes with value 1.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample2.png)

    ```
    Input: nums = [5], head = [1,2,3,4]
    Output: [1,2,3,4]
    Explanation: No node has value 5.
    ```

    ## Constraints

    - 1 <= nums.length <= 10<sup>5</sup>
    - 1 <= nums[i] <= 10<sup>5</sup>
    - All elements in nums are unique.
    - The number of nodes in the given list is in the range [1, 10<sup>5</sup>].
    - 1 <= Node.val <= 10<sup>5</sup>
    - The input is generated such that there is at least one node in the linked list that has a value not present in nums.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def modified_list(self, nums: list[int], head: ListNode[int] | None) -> ListNode[int] | None:
            raise NotImplementedError('Implement modified_list')

    practice_exports = {'ListNode': ListNode, 'Solution': Solution}
    return (practice_exports,)


@app.cell(hide_code=True)
def _(mo):
    run_tests = mo.ui.run_button(label="Run tests")
    run_tests
    return (run_tests,)


@app.cell(hide_code=True)
def _(mo, practice_exports, run_practice_tests, run_tests):
    mo.stop(not run_tests.value, mo.md("Implement your solution, then run the tests."))
    test_result = run_practice_tests(mo.notebook_dir(), practice_exports)
    mo.vstack([
        mo.md(f"**{test_result.passed} passed · {test_result.failed} failed · "
              f"{test_result.skipped} skipped**"),
        mo.md("**All tests passed.**" if test_result.exit_code == 0 else "**Tests are not passing yet.**"),
        mo.accordion({"Test output": mo.plain_text(test_result.output)}),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Notes

    Record your approach, complexity, and edge cases here.
    """)
    return


if __name__ == "__main__":
    app.run()
