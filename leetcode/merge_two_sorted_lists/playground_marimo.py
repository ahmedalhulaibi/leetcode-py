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
    # 21. Merge Two Sorted Lists

    **Easy** · Linked List, Recursion

    You are given the heads of two sorted linked lists `list1` and `list2`.

    Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

    Return *the head of the merged linked list*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

    ```
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    ```

    ```
    Input: list1 = [], list2 = []
    Output: []
    ```

    ```
    Input: list1 = [], list2 = [0]
    Output: [0]
    ```

    ## Constraints

    - The number of nodes in both lists is in the range `[0, 50]`.
    - `-100 <= Node.val <= 100`
    - Both `list1` and `list2` are sorted in **non-decreasing** order.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def merge_two_lists(self, list1: ListNode[int] | None, list2: ListNode[int] | None) -> ListNode[int] | None:
            raise NotImplementedError('Implement merge_two_lists')

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
