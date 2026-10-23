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
    # 1361. Validate Binary Tree Nodes

    **Medium** · Tree, Depth-First Search, Breadth-First Search, Union Find, Graph

    You have <code>n</code> binary tree nodes numbered from <code>0</code> to <code>n - 1</code> where node <code>i</code> has two children <code>leftChild[i]</code> and <code>rightChild[i]</code>, return <code>true</code> if and only if all the given nodes form <strong>exactly one valid binary tree</strong>.

    If node <code>i</code> has no left child then <code>leftChild[i]</code> will equal <code>-1</code>, similarly for the right child.

    Note that the nodes have no values and that we only use the node numbers in this problem.

    ## Examples

    ```
    Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
    Output: true
    ```

    ```
    Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
    Output: false
    ```

    ```
    Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
    Output: false
    ```

    ## Constraints

    - n == leftChild.length == rightChild.length
    - 1 <= n <= 10^4
    - -1 <= leftChild[i], rightChild[i] <= n - 1



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def validate_binary_tree_nodes(self, n: int, left_child: list[int], right_child: list[int]) -> bool:
            raise NotImplementedError('Implement validate_binary_tree_nodes')

    practice_exports = {'Solution': Solution}
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
