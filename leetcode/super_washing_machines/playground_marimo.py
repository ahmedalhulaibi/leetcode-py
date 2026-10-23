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
    # 517. Super Washing Machines

    **Hard** · Array, Greedy

    You have `n` super washing machines on a line. Initially, each washing machine has some dresses or is empty.

    For each move, you could choose any `m` (`1 <= m <= n`) washing machines, and pass one dress of each washing machine to one of its adjacent washing machines at the same time.

    Given an integer array `machines` representing the number of dresses in each washing machine from left to right on the line, return the minimum number of moves to make all the washing machines have the same number of dresses. If it is not possible to do it, return `-1`.

    ## Examples

    ```
    Input: machines = [1,0,5]
    Output: 3
    Explanation:
    1st move:    1     0 <-- 5    =>    1     1     4
    2nd move:    1 <-- 1 <-- 4    =>    2     1     3
    3rd move:    2     1 <-- 3    =>    2     2     2
    ```

    ```
    Input: machines = [0,3,0]
    Output: 2
    Explanation:
    1st move:    0 <-- 3     0    =>    1     2     0
    2nd move:    1     2 --> 0    =>    1     1     1
    ```

    ```
    Input: machines = [0,2,0]
    Output: -1
    Explanation:
    It's impossible to make all three washing machines have the same number of dresses.
    ```

    ## Constraints

    - n == machines.length
    - 1 <= n <= 10^4
    - 0 <= machines[i] <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_min_moves(self, machines: list[int]) -> int:
            raise NotImplementedError('Implement find_min_moves')

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
