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
    # 1669. Merge In Between Linked Lists

    **Medium** · Linked List

    You are given two linked lists: `list1` and `list2` of sizes `n` and `m` respectively.

    Remove `list1`'s nodes from the `a<sup>th</sup>` node to the `b<sup>th</sup>` node, and put `list2` in their place.

    The blue edges and nodes in the following figure indicate the result:

    ![Example 1](https://assets.leetcode.com/uploads/2020/11/05/fig1.png)

    Build the result list and return its head.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2024/03/01/ll.png)

    ```
    Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
    Output: [10,1,13,1000000,1000001,1000002,5]
    Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/11/05/merge_linked_list_ex2.png)

    ```
    Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
    Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
    ```

    ## Constraints

    - `3 <= list1.length <= 10^4`
    - `1 <= a <= b < list1.length - 1`
    - `1 <= list2.length <= 10^4`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def merge_in_between(self, list1: ListNode[int] | None, a: int, b: int, list2: ListNode[int] | None) -> ListNode[int] | None:
            raise NotImplementedError('Implement merge_in_between')

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
