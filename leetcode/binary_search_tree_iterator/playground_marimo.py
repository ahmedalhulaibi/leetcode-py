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
    # 173. Binary Search Tree Iterator

    **Medium** · Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator

    Implement the `BSTIterator` class that represents an iterator over the **in-order traversal** of a binary search tree (BST):

    - `BSTIterator(TreeNode root)` Initializes an object of the `BSTIterator` class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
    - `boolean hasNext()` Returns `true` if there exists a number in the traversal to the right of the pointer, otherwise returns `false`.
    - `int next()` Moves the pointer to the right, then returns the number at the pointer.

    Notice that by initializing the pointer to a non-existent smallest number, the first call to `next()` will return the smallest element in the BST.

    You may assume that `next()` calls will always be valid. That is, there will be at least a next number in the in-order traversal when `next()` is called.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png)

    ```
    Input
    ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
    Output
    [null, 3, 7, true, 9, true, 15, true, 20, false]

    Explanation
    BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
    bSTIterator.next();    // return 3
    bSTIterator.next();    // return 7
    bSTIterator.hasNext(); // return True
    bSTIterator.next();    // return 9
    bSTIterator.hasNext(); // return True
    bSTIterator.next();    // return 15
    bSTIterator.hasNext(); // return True
    bSTIterator.next();    // return 20
    bSTIterator.hasNext(); // return False
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 10<sup>5</sup>]
    - 0 <= Node.val <= 10<sup>6</sup>
    - At most 10<sup>5</sup> calls will be made to hasNext, and next.

    **Follow up:**

    - Could you implement `next()` and `hasNext()` to run in average `O(1)` time and use `O(h)` memory, where `h` is the height of the tree?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class BSTIterator:

        def __init__(self, root: TreeNode[int] | None) -> None:
            raise NotImplementedError('Implement __init__')

        def next(self) -> int:
            raise NotImplementedError('Implement next')

        def has_next(self) -> bool:
            raise NotImplementedError('Implement has_next')

    practice_exports = {'TreeNode': TreeNode, 'BSTIterator': BSTIterator}
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
