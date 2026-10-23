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
    mo.md(r"""
    # 1273. Delete Tree Nodes

    **Medium** · Tree, Depth-First Search, Breadth-First Search, Array, Tree DP

    A tree rooted at node 0 is given as follows:

    <ul>
        <li>The number of nodes is <code>nodes</code>;</li>
        <li>The value of the <code>i<sup>th</sup></code> node is <code>value[i]</code>;</li>
        <li>The parent of the <code>i<sup>th</sup></code> node is <code>parent[i]</code>.</li>
    </ul>

    <p>Remove every subtree whose sum of values of nodes is zero.</p>

    <p>Return <em>the number of the remaining nodes in the tree</em>.</p>

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1273.Delete%20Tree%20Nodes/images/1421_sample_1.png)

    ```
    Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
    Output: 2
    ```

    ```
    Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]
    Output: 6
    ```

    ## Constraints

    - 1 <= nodes <= 10^4
    - parent.length == nodes
    - 0 <= parent[i] <= nodes - 1
    - parent[0] == -1 which indicates that 0 is the root.
    - value.length == nodes
    - -10^5 <= value[i] <= 10^5
    - The given input is <strong>guaranteed</strong> to represent a <strong>valid tree</strong>.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def delete_tree_nodes(self, nodes: int, parent: list[int], value: list[int]) -> int:
            raise NotImplementedError('Implement delete_tree_nodes')

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
