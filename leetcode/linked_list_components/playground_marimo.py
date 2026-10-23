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
    # 817. Linked List Components

    **Medium** · Array, Hash Table, Linked List

    You are given the `head` of a linked list containing unique integer values and an integer array `nums` that is a subset of the linked list values.

    Return the number of **connected components** in `nums`. A connected component is a non-empty, maximal sequence of **consecutive** nodes in the linked list such that every node's value belongs to `nums`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom1.jpg)

    ```
    Input: head = [0,1,2,3], nums = [0,1,3]
    Output: 2
    Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom2.jpg)

    ```
    Input: head = [0,1,2,3,4], nums = [0,3,1,4]
    Output: 2
    Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
    ```

    ## Constraints

    - The number of nodes in the linked list is n.
    - 1 <= n <= 10<sup>4</sup>
    - 0 <= Node.val < n
    - All the values Node.val are unique.
    - 1 <= nums.length <= n
    - 0 <= nums[i] < n
    - All the values of nums are unique.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def num_components(self, head: ListNode[int] | None, nums: list[int]) -> int:
            raise NotImplementedError('Implement num_components')

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
