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
    # 1506. Find Root of N-Ary Tree

    **Medium** · Bit Manipulation, Tree, Depth-First Search, Hash Table

    You are given all the nodes of an **N-ary tree** as an array of `Node` objects, where each node has a **unique value**.

    Return *the **root** of the N-ary tree*.

    **Custom testing:**

    An N-ary tree can be serialized as represented in its level order traversal where each group of children is separated by the `null` value (see examples).

    ![Example 1](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

    For example, the above tree is serialized as `[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`.

    The testing will be done in the following way:

    1. The **input data** should be provided as a serialization of the tree.
    2. The driver code will construct the tree from the serialized input data and put each `Node` object into an array **in an arbitrary order**.
    3. The driver code will pass the array to `findRoot`, and your function should find and return the root `Node` object in the array.
    4. The driver code will take the returned `Node` object and serialize it. If the serialized value and the input data are the **same**, the test **passes**.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

    ```
    Input: tree = [1,null,3,2,4,null,5,6]
    Output: [1,null,3,2,4,null,5,6]
    Explanation: The tree from the input data is shown above.
    The driver code creates the tree and gives findRoot the Node objects in an arbitrary order.
    For example, the passed array could be [Node(5),Node(4),Node(3),Node(6),Node(2),Node(1)] or [Node(2),Node(6),Node(1),Node(3),Node(5),Node(4)].
    The findRoot function should return the root Node(1), and the driver code will serialize it and compare with the input data.
    The input data and serialized Node(1) are the same, so the test passes.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)

    ```
    Input: tree = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    ```

    ## Constraints

    - The total number of nodes is between `[1, 5 * 10^4]`.
    - Each node has a **unique** value.

    **Follow up:** Could you solve this problem in constant space complexity with a linear time algorithm?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Node:

        def __init__(self, val: 'int'=0, children: 'list[Node] | None'=None) -> 'None':
            self.val = val
            self.children = children if children is not None else []

    class Solution:

        def find_root(self, tree: 'list[Node]') -> 'Node':
            raise NotImplementedError('Implement find_root')

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
