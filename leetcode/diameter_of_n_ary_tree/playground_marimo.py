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
    # 1522. Diameter of N-Ary Tree

    **Medium** · Tree, Depth-First Search, Tree DP

    Given a `root` of an `N-ary tree`, you need to compute the length of the diameter of the tree.

    The diameter of an N-ary tree is the length of the **longest** path between any two nodes in the tree. This path may or may not pass through the `root`.

    *(Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)*

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1522.Diameter%20of%20N-Ary%20Tree/images/sample_2_1897.png)

    ```
    Input: root = [1,null,3,2,4,null,5,6]
    Output: 3
    Explanation: Diameter is shown in red color.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1522.Diameter%20of%20N-Ary%20Tree/images/sample_1_1897.png)

    ```
    Input: root = [1,null,2,null,3,4,null,5,null,6]
    Output: 4
    ```

    ![Example 3](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1522.Diameter%20of%20N-Ary%20Tree/images/sample_3_1897.png)

    ```
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: 7
    ```

    ## Constraints

    - The depth of the n-ary tree is less than or equal to `1000`.
    - The total number of nodes is between `[1, 10^4]`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class NaryNode:

        def __init__(self, val: 'int'=0, children: 'list[NaryNode] | None'=None) -> 'None':
            self.val = val
            self.children = children if children is not None else []

    class Solution:

        def diameter(self, root: 'NaryNode | None') -> 'int':
            raise NotImplementedError('Implement diameter')

    practice_exports = {'NaryNode': NaryNode, 'Solution': Solution}
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
