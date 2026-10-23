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
    # 510. Inorder Successor in BST II

    **Medium** · Tree, Binary Search Tree, Binary Tree

    Given a `node` in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return `null`.

    The successor of a `node` is the node with the smallest key greater than `node.val`.

    You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for `Node`:

    ```
    class Node {
        public int val;
        public Node left;
        public Node right;
        public Node parent;
    }
    ```

    **Follow up:** Could you solve it without looking up any of the node's values?

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0510.Inorder%20Successor%20in%20BST%20II/images/285_example_1.png)

    ```
    Input: tree = [2,1,3], node = 1
    Output: 2
    Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0500-0599/0510.Inorder%20Successor%20in%20BST%20II/images/285_example_2.png)

    ```
    Input: tree = [5,3,6,2,4,null,null,1], node = 6
    Output: null
    Explanation: There is no in-order successor of the current node, so the answer is null.
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[1, 10^4]`.
    - `-10^5 <= Node.val <= 10^5`
    - All Nodes will have unique values.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Node:

        def __init__(self, val: 'int'=0) -> 'None':
            self.val = val
            self.left: 'Node | None' = None
            self.right: 'Node | None' = None
            self.parent: 'Node | None' = None

    class Solution:

        def inorder_successor(self, node: 'Node') -> 'Node | None':
            raise NotImplementedError('Implement inorder_successor')

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
