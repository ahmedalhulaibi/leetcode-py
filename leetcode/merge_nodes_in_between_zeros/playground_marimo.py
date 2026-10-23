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
    # 2181. Merge Nodes in Between Zeros

    **Medium** · Linked List, Simulation

    You are given the <code>head</code> of a linked list, which contains a series of integers <strong>separated</strong> by <code>0</code>'s. The <strong>beginning</strong> and <strong>end</strong> of the linked list will have <code>Node.val == 0</code>.

    For <strong>every</strong> two consecutive <code>0</code>'s, <strong>merge</strong> all the nodes lying in between them into a single node whose value is the <strong>sum</strong> of all the merged nodes. The modified list should not contain any <code>0</code>'s.

    Return <em>the head of the modified linked list</em>.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/02/02/ex1-1.png)

    ```
    Input: head = [0,3,1,0,4,5,2,0]
    Output: [4,11]
    Explanation: The modified list contains the sum of the nodes marked in green: 3 + 1 = 4, and the sum of the nodes marked in red: 4 + 5 + 2 = 11.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/02/02/ex2-1.png)

    ```
    Input: head = [0,1,0,3,0,2,2,0]
    Output: [1,3,4]
    Explanation: The modified list contains the sum of the nodes marked in green: 1 = 1, the sum of the nodes marked in red: 3 = 3, and the sum of the nodes marked in yellow: 2 + 2 = 4.
    ```

    ## Constraints

    - The number of nodes in the list is in the range `[3, 2 * 10^5]`.
    - `0 <= Node.val <= 1000`
    - There are no two consecutive nodes with `Node.val == 0`.
    - The beginning and end of the linked list have `Node.val == 0`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def merge_nodes(self, head: ListNode[int] | None) -> ListNode[int] | None:
            raise NotImplementedError('Implement merge_nodes')

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
