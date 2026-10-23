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
    # 919. Complete Binary Tree Inserter

    **Medium** · Tree, Breadth-First Search, Design, Binary Tree

    A **complete binary tree** is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

    Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

    Implement the `CBTInserter` class:

    - `CBTInserter(TreeNode root)` Initializes the data structure with the `root` of the complete binary tree.
    - `int insert(int val)` Inserts a `TreeNode` into the tree with value `Node.val == val` so that the tree remains complete, and returns the value of the parent of the inserted `TreeNode`.
    - `TreeNode get_root()` Returns the root node of the tree.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/08/03/lc-treeinsert.jpg)

    ```
    Input
    ["CBTInserter", "insert", "insert", "get_root"]
    [[[1, 2]], [3], [4], []]
    Output
    [null, 1, 2, [1, 2, 3, 4]]

    Explanation
    CBTInserter cBTInserter = new CBTInserter([1, 2]);
    cBTInserter.insert(3);  // return 1
    cBTInserter.insert(4);  // return 2
    cBTInserter.get_root(); // return [1, 2, 3, 4]
    ```

    ## Constraints

    - The number of nodes in the tree will be in the range `[1, 1000]`.
    - `0 <= Node.val <= 5000`
    - `root` is a complete binary tree.
    - `0 <= val <= 5000`
    - At most `10^4` calls will be made to `insert` and `get_root`.

    **Follow up:** Can you implement `insert` in `O(1)` time per call, using the structure of a complete binary tree?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class CBTInserter:

        def __init__(self, root: TreeNode[int] | None) -> None:
            raise NotImplementedError('Implement __init__')

        def insert(self, val: int) -> int:
            raise NotImplementedError('Implement insert')

        def get_root(self) -> TreeNode[int] | None:
            raise NotImplementedError('Implement get_root')

    practice_exports = {'TreeNode': TreeNode, 'CBTInserter': CBTInserter}
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
