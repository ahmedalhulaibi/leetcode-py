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
    # 23. Merge k Sorted Lists

    **Hard** · Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort

    You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

    *Merge all the linked-lists into one sorted linked-list and return it.*

    ## Examples

    ```
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    ```
    **Explanation:** The linked-lists are:
    ```
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    ```
    merging them into one sorted linked list:
    ```
    1->1->2->3->4->4->5->6
    ```

    ```
    Input: lists = []
    Output: []
    ```

    ```
    Input: lists = [[]]
    Output: []
    ```

    ## Constraints

    - `k == lists.length`
    - `0 <= k <= 10^4`
    - `0 <= lists[i].length <= 500`
    - `-10^4 <= lists[i][j] <= 10^4`
    - `lists[i]` is sorted in ascending order.
    - The sum of `lists[i].length` will not exceed `10^4`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def merge_k_lists(self, lists: list[ListNode[int] | None]) -> ListNode[int] | None:
            raise NotImplementedError('Implement merge_k_lists')

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
