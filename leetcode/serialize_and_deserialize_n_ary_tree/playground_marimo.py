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
    # 428. Serialize and Deserialize N-ary Tree

    **Hard** · Tree, Depth-First Search, Breadth-First Search, String

    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

    For example, you may serialize the following `3-ary` tree as `[1 [3[5 6] 2 4]]`. Note that this is just an example, you do not necessarily need to follow this format.

    Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated by the null value. For example, the above tree may be serialized as `[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`.

    You do not necessarily need to follow the above-suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0428.Serialize%20and%20Deserialize%20N-ary%20Tree/images/narytreeexample.png)

    ```
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0428.Serialize%20and%20Deserialize%20N-ary%20Tree/images/sample_4_964.png)

    ```
    Input: root = [1,null,3,2,4,null,5,6]
    Output: [1,null,3,2,4,null,5,6]
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
    class Node:

        def __init__(self, val: 'int'=0, children: 'list[Node] | None'=None) -> 'None':
            self.val = val
            self.children = children if children is not None else []

    class Codec:

        def __init__(self) -> 'None':
            raise NotImplementedError('Implement __init__')

        def encode(self, root: 'Node | None') -> 'str':
            raise NotImplementedError('Implement encode')

        def decode(self, data: 'str') -> 'Node | None':
            raise NotImplementedError('Implement decode')

    practice_exports = {'Node': Node, 'Codec': Codec}
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
