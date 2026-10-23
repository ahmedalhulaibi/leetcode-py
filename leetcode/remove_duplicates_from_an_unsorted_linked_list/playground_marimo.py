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
    # 1836. Remove Duplicates From an Unsorted Linked List

    **Medium** · Hash Table, Linked List

    Given the `head` of a linked list, find all the values that appear **more than once** in the list and delete the nodes that have any of those values.

    Return *the linked list after the deletions*.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1800-1899/1836.Remove%20Duplicates%20From%20an%20Unsorted%20Linked%20List/images/tmp-linked-list.jpg)

    ```
    Input: head = [1,2,3,2]
    Output: [1,3]
    Explanation: 2 appears twice in the linked list, so all 2's should be deleted. After deleting all 2's, we are left with [1,3].
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1800-1899/1836.Remove%20Duplicates%20From%20an%20Unsorted%20Linked%20List/images/tmp-linked-list-1.jpg)

    ```
    Input: head = [2,1,1,2]
    Output: []
    Explanation: 2 and 1 both appear twice. All the elements should be deleted.
    ```

    ![Example 3](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1800-1899/1836.Remove%20Duplicates%20From%20an%20Unsorted%20Linked%20List/images/tmp-linked-list-2.jpg)

    ```
    Input: head = [3,2,2,1,3,2,4]
    Output: [1,4]
    Explanation: 3 appears twice and 2 appears three times. After deleting all 3's and 2's, we are left with [1,4].
    ```

    ## Constraints

    - The number of nodes in the list is in the range `[1, 10^5]`.
    - `1 <= Node.val <= 10^5`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def delete_duplicates_unsorted(self, head: ListNode[int] | None) -> ListNode[int] | None:
            raise NotImplementedError('Implement delete_duplicates_unsorted')

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
