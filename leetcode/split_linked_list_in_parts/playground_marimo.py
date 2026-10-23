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
    # 725. Split Linked List in Parts

    **Medium** · Linked List

    Given the head of a singly linked list and an integer `k`, split the linked list into `k` consecutive linked list parts.

    The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

    The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

    Return an array of the `k` parts.

    ## Examples

    ```
    Input: head = [1,2,3], k = 5
    Output: [[1],[2],[3],[],[]]
    Explanation: The first element output[0] has output[0].val = 1, output[0].next = null.
    The last element output[4] is null, but its string representation as a ListNode is [].
    ```

    ```
    Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
    Output: [[1,2,3,4],[5,6,7],[8,9,10]]
    Explanation: The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
    ```

    ## Constraints

    - The number of nodes in the list is in the range [0, 1000].
    - 0 <= Node.val <= 1000
    - 1 <= k <= 50



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def split_list_to_parts(self, head: ListNode[int] | None, k: int) -> list[ListNode[int] | None]:
            raise NotImplementedError('Implement split_list_to_parts')

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
