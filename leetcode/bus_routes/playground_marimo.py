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
    # 815. Bus Routes

    **Hard** · Array, Hash Table, Breadth-First Search

    You are given an array `routes` representing bus routes where `routes[i]` is a bus route that the `i^th` bus repeats forever.

    - For example, if `routes[0] = [1, 5, 7]`, this means that the `0^th` bus travels in the sequence `1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ...` forever.

    You will start at the bus stop `source` (You are not on any bus initially), and you want to go to the bus stop `target`. You can travel between bus stops by buses only.

    Return the least number of buses you must take to travel from `source` to `target`. Return `-1` if it is not possible.

    ## Examples

    ```
    Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
    Output: 2
    Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
    ```

    ```
    Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
    Output: -1
    ```

    ## Constraints

    - 1 <= routes.length <= 500
    - 1 <= routes[i].length <= 10^5
    - All the values of `routes[i]` are **unique**.
    - sum(routes[i].length) <= 10^5
    - 0 <= routes[i][j] < 10^6
    - 0 <= source, target < 10^6



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_buses_to_destination(self, routes: list[list[int]], source: int, target: int) -> int:
            raise NotImplementedError('Implement num_buses_to_destination')

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
