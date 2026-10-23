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
    # 1269. Number of Ways to Stay in the Same Place After Some Steps

    **Hard** · Dynamic Programming

    You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

    Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 10^9 + 7.

    ## Examples

    ```
    Input: steps = 3, arrLen = 2
    Output: 4
    Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
    - Right, Left, Stay
    - Stay, Right, Left
    - Right, Stay, Left
    - Stay, Stay, Stay
    ```

    ```
    Input: steps = 2, arrLen = 4
    Output: 2
    Explanation: There are 2 differents ways to stay at index 0 after 2 steps
    - Right, Left
    - Stay, Stay
    ```

    ```
    Input: steps = 4, arrLen = 2
    Output: 8
    ```

    ## Constraints

    - 1 <= steps <= 500
    - 1 <= arrLen <= 10^6



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_ways(self, steps: int, arr_len: int) -> int:
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
