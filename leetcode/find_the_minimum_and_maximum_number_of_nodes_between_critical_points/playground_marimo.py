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
    # 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

    **Medium** · Linked List

    A **critical point** in a linked list is defined as **either** a **local maxima** or a **local minima**.

    A node is a **local maxima** if the current node has a value **strictly greater** than the previous node and the next node.

    A node is a **local minima** if the current node has a value **strictly smaller** than the previous node and the next node.

    Note that a node can only be a local maxima/minima if there exists **both** a previous node and a next node.

    Given a linked list `head`, return *an array of length 2 containing* `[minDistance, maxDistance]` *where* `minDistance` *is the* ***minimum distance*** *between* ***any two distinct*** *critical points and* `maxDistance` *is the* ***maximum distance*** *between* ***any two distinct*** *critical points. If there are* ***fewer*** *than two critical points, return* `[-1, -1]`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/10/13/a1.png)

    ```
    Input: head = [3,1]
    Output: [-1,-1]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/10/13/a2.png)

    ```
    Input: head = [5,3,1,2,5,1,2]
    Output: [1,3]
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/10/14/a5.png)

    ```
    Input: head = [1,3,2,2,3,2,2,2,7]
    Output: [3,3]
    ```

    ## Constraints

    - The number of nodes in the list is in the range `[2, 10^5]`.
    - `1 <= Node.val <= 10^5`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import ListNode

    class Solution:

        def nodes_between_critical_points(self, head: ListNode[int] | None) -> list[int]:
            raise NotImplementedError('Implement nodes_between_critical_points')

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
