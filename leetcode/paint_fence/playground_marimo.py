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
    # 276. Paint Fence

    **Medium** · Dynamic Programming

    You are painting a fence of `n` posts with `k` different colors. You must paint the posts following these rules:

    - Every post must be painted **exactly one** color.
    - There **cannot** be three or more **consecutive** posts with the same color.

    Given the two integers `n` and `k`, return *the **number of ways** you can paint the fence*.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0276.Paint%20Fence/images/paintfenceex1.png)

    ```
    Input: n = 3, k = 2
    Output: 6
    Explanation: All the possibilities are shown.
    Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.
    ```

    ```
    Input: n = 1, k = 1
    Output: 1
    ```

    ```
    Input: n = 7, k = 2
    Output: 42
    ```

    ## Constraints

    - `1 <= n <= 50`
    - `1 <= k <= 10^5`
    - The testcases are generated such that the answer is in the range `[0, 2^31 - 1]` for the given `n` and `k`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_ways(self, n: int, k: int) -> int:
            raise NotImplementedError('Implement num_ways')

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
