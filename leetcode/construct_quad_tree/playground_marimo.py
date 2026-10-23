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
    # 427. Construct Quad Tree

    **Medium** · Array, Divide and Conquer, Tree, Matrix

    Given a `n * n` matrix `grid` of `0's` and `1's` only. We want to represent `grid` with a Quad-Tree.

    Return _the root of the Quad-Tree representing `grid`_.

    A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

    - `val`: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the `val` to True or False when `isLeaf` is False, and both are accepted in the answer.
    - `isLeaf`: True if the node is a leaf node on the tree or False if the node has four children.

    ```
    class Node {
        public boolean val;
        public boolean isLeaf;
        public Node topLeft;
        public Node topRight;
        public Node bottomLeft;
        public Node bottomRight;
    }
    ```

    We can construct a Quad-Tree from a two-dimensional area using the following steps:

    1. If the current grid has the same value (i.e all `1's` or all `0's`) set `isLeaf` True and set `val` to the value of the grid and set the four children to Null and stop.
    2. If the current grid has different values, set `isLeaf` to False and set `val` to any value and divide the current grid into four sub-grids as shown in the photo.
    3. Recurse for each of the children with the proper sub-grid.

    **Quad-Tree format:** The output represents the serialized format of a Quad-Tree using level order traversal, where `null` signifies a path terminator where no node exists below. The node is represented as a list `[isLeaf, val]`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/02/11/grid1.png)

    ```
    Input: grid = [[0,1],[1,0]]
    Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
    Explanation: The root is not a leaf. Its four children (top-left, top-right, bottom-left, bottom-right) are leaves.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/02/12/e2mat.png)

    ```
    Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
    ```

    ## Constraints

    - n == grid.length == grid[i].length
    - n == 2^x where 0 <= x <= 6



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Node:

        def __init__(self, val: 'bool', isLeaf: 'bool', topLeft: 'Node | None'=None, topRight: 'Node | None'=None, bottomLeft: 'Node | None'=None, bottomRight: 'Node | None'=None) -> 'None':
            self.val = val
            self.isLeaf = isLeaf
            self.topLeft = topLeft
            self.topRight = topRight
            self.bottomLeft = bottomLeft
            self.bottomRight = bottomRight

    class Solution:

        def construct(self, grid: 'list[list[int]]') -> 'Node':
            raise NotImplementedError('Implement construct')

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
