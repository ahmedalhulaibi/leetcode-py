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
    # 117. Populating Next Right Pointers in Each Node II

    **Medium** · Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree

    Given a binary tree

    ```
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
    ```

    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

    Initially, all next pointers are set to `NULL`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/02/15/117_sample.png)

    ```
    Input: root = [1,2,3,4,5,null,7]
    Output: [1,#,2,3,#,4,5,7,#]
    Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
    ```

    ```
    Input: root = []
    Output: []
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [0, 6000]
    - -100 <= Node.val <= 100

    **Follow-up:**

    - You may only use constant extra space.
    - The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Node:

        def __init__(self, val: 'int'=0, left: 'Node | None'=None, right: 'Node | None'=None, next: 'Node | None'=None):
            self.val = val
            self.left = left
            self.right = right
            self.next = next

    class Solution:

        def connect(self, root: 'Node | None') -> 'Node | None':
            raise NotImplementedError('Implement connect')

    practice_exports = {'Node': Node, 'Solution': Solution}
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
