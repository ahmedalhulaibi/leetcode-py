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
    # 1650. Lowest Common Ancestor of a Binary Tree III

    **Medium** · Tree, Hash Table, Two Pointers, Binary Tree, Lowest Common Ancestor

    Given two nodes of a binary tree `p` and `q`, return *their* *lowest common ancestor (LCA)*.

    Each node will have a reference to its parent node. The definition for `Node` is below:

    ```
    class Node {
        public int val;
        public Node left;
        public Node right;
        public Node parent;
    }
    ```

    According to the **definition of LCA on Wikipedia**: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1600-1699/1650.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20III/images/binarytree.png)

    ```
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1600-1699/1650.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20III/images/binarytree.png)

    ```
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
    ```

    ```
    Input: root = [1,2], p = 1, q = 2
    Output: 1
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[2, 10^5]`.
    - `-10^9 <= Node.val <= 10^9`
    - All `Node.val` are **unique**.
    - `p != q`
    - `p` and `q` exist in the tree.

    **Follow up:** Can you find the LCA without using any extra space (excluding recursion) and without knowing the root of the tree?

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

        def lowest_common_ancestor(self, p: 'Node', q: 'Node') -> 'Node':
            raise NotImplementedError('Implement lowest_common_ancestor')

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
