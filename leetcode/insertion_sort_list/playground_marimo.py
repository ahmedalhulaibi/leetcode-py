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
    # 147. Insertion Sort List

    **Medium** · Linked List, Sorting

    Given the `head` of a singly linked list, sort the list using **insertion sort**, and return *the sorted list's head*.

    The steps of the **insertion sort** algorithm:

    1. Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
    2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
    3. It repeats until no input elements remain.

    The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

    ![Insertion Sort Example](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/03/04/sort1linked-list.jpg)

    ```
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/03/04/sort2linked-list.jpg)

    ```
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]
    ```

    ## Constraints

    - The number of nodes in the list is in the range [1, 5000]
    - -5000 <= Node.val <= 5000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def insertion_sort_list(self, head: ListNode[int] | None) -> ListNode[int] | None:
            raise NotImplementedError('Implement insertion_sort_list')

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
