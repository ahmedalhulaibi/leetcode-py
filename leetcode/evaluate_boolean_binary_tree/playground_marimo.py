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
    # 2331. Evaluate Boolean Binary Tree

    **Easy** · Tree, Depth-First Search, Binary Tree

    You are given the `root` of a **full binary tree** with the following properties:

    - **Leaf nodes** have either the value `0` or `1`, where `0` represents `False` and `1` represents `True`.
    - **Non-leaf nodes** have either the value `2` or `3`, where `2` represents the boolean `OR` and `3` represents the boolean `AND`.

    The **evaluation** of a node is as follows:

    - If the node is a leaf node, the evaluation is the **value** of the node, i.e. `True` or `False`.
    - Otherwise, **evaluate** the node's two children and **apply** the boolean operation of its value with the children's evaluations.

    Return *the boolean result of **evaluating** the* `root` *node*.

    A **full binary tree** is a binary tree where each node has either `0` or `2` children.

    A **leaf node** is a node that has zero children.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/05/16/example1drawio1.png)

    ```
    Input: root = [2,1,3,null,null,0,1]
    Output: true
    Explanation: The above diagram illustrates the evaluation process.
    The AND node evaluates to False AND True = False.
    The OR node evaluates to True OR False = True.
    The root node evaluates to True, so we return true.
    ```

    ```
    Input: root = [0]
    Output: false
    Explanation: The root node is a leaf node and it evaluates to false, so we return false.
    ```

    ## Constraints

    - The number of nodes in the tree is in the range [1, 1000].
    - 0 <= Node.val <= 3
    - Every node has either 0 or 2 children.
    - Leaf nodes have a value of 0 or 1.
    - Non-leaf nodes have a value of 2 or 3.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import TreeNode

    class Solution:

        def evaluate_tree(self, root: TreeNode[int] | None) -> bool:
            raise NotImplementedError('Implement evaluate_tree')

    practice_exports = {'TreeNode': TreeNode, 'Solution': Solution}
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
