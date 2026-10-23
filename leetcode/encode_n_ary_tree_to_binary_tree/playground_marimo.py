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
    # 431. Encode N-ary Tree to Binary Tree

    **Hard** · Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree

    Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-ary tree structure.

    Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.

    For example, you may encode the following `3-ary` tree to a binary tree in this way: `Input: root = [1,null,3,2,4,null,5,6]`. Note that the above is just an example which *might or might not* work. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0431.Encode%20N-ary%20Tree%20to%20Binary%20Tree/images/narytreebinarytreeexample.png)

    ```
    Input: root = [1,null,3,2,4,null,5,6]
    Output: [1,null,3,2,4,null,5,6]
    ```

    ```
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    ```

    ```
    Input: root = []
    Output: []
    ```

    ## Constraints

    - The number of nodes in the tree is in the range `[0, 10^4]`.
    - `0 <= Node.val <= 10^4`.
    - The height of the n-ary tree is less than or equal to `1000`.
    - Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Node:

        def __init__(self, val: 'int'=0, children: 'list[Node] | None'=None) -> 'None':
            self.val = val
            self.children = children if children is not None else []

    class Codec:

        def __init__(self) -> 'None':
            raise NotImplementedError('Implement __init__')

        def encode(self, root: 'Node | None') -> 'TreeNode[int] | None':
            raise NotImplementedError('Implement encode')

        def decode(self, data: 'TreeNode[int] | None') -> 'Node | None':
            raise NotImplementedError('Implement decode')

    practice_exports = {'TreeNode': TreeNode, 'Node': Node, 'Codec': Codec}
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
