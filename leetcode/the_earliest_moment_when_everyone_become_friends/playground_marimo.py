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
    # 1101. The Earliest Moment When Everyone Become Friends

    **Medium** · Array, Union Find, Sorting

    There are `n` people in a social group labeled from `0` to `n - 1`. You are given an array `logs` where `logs[i] = [timestampi, xi, yi]` indicates that `xi` and `yi` will be friends at the time `timestampi`.

    Friendship is **symmetric**. That means if `a` is friends with `b`, then `b` is friends with `a`. Also, person `a` is **acquainted** with a person `b` if `a` is friends with `b`, or `a` is a friend of someone acquainted with `b`.

    Return *the earliest time for which every person became acquainted with every other person*. If there is no such earliest time, return `-1`.

    ## Examples

    ```
    Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
    Output: 20190301
    Explanation: After the event at timestamp 20190301, every person becomes acquainted with every other person.
    ```

    ```
    Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
    Output: 3
    ```

    ## Constraints

    - 2 <= n <= 100
    - 1 <= logs.length <= 10^4
    - logs[i].length == 3
    - 0 <= timestampi <= 10^9
    - 0 <= xi, yi <= n - 1
    - xi != yi
    - All the values timestampi are unique.
    - All the pairs (xi, yi) occur at most one time in the input.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def earliest_acq(self, logs: list[list[int]], n: int) -> int:
            raise NotImplementedError('Implement earliest_acq')

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
