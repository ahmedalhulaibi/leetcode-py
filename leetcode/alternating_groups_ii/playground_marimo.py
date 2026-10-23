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
    # 3208. Alternating Groups II

    **Medium** · Array, Sliding Window

    There is a circle of red and blue tiles. You are given an array of integers <code>colors</code> and an integer <code>k</code>. The color of tile <code>i</code> is represented by <code>colors[i]</code>:

    <ul>
        <li><code>colors[i] == 0</code> means that tile <code>i</code> is <strong>red</strong>.</li>
        <li><code>colors[i] == 1</code> means that tile <code>i</code> is <strong>blue</strong>.</li>
    </ul>

    <p>An <strong>alternating</strong> group is every <code>k</code> contiguous tiles in the circle with <strong>alternating</strong> colors (each tile in the group except the first and last one has a different color from its <strong>left</strong> and <strong>right</strong> tiles).</p>

    <p>Return the number of <strong>alternating</strong> groups.</p>

    <p><strong>Note</strong> that since <code>colors</code> represents a <strong>circle</strong>, the <strong>first</strong> and the <strong>last</strong> tiles are considered to be next to each other.</p>

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183519.png)

    ```
    Input: colors = [0,1,0,1,0], k = 3
    Output: 3
    ```

    Alternating groups:

    ![Group 1](https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-182448.png)

    ![Group 2](https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-182844.png)

    ![Group 3](https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-183057.png)

    ![Example 2](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183907.png)

    ```
    Input: colors = [0,1,0,0,1,0,1], k = 6
    Output: 2
    ```

    Alternating groups:

    ![Group 1](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184128.png)

    ![Group 2](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184240.png)

    ![Example 3](https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184516.png)

    ```
    Input: colors = [1,1,0,1], k = 4
    Output: 0
    ```

    ## Constraints

    - 3 <= colors.length <= 10^5
    - 0 <= colors[i] <= 1
    - 3 <= k <= colors.length



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def number_of_alternating_groups(self, colors: list[int], k: int) -> int:
            raise NotImplementedError('Implement number_of_alternating_groups')

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
