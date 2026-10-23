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
    # 933. Number of Recent Calls

    **Easy** · Design, Queue, Data Stream

    You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

    Implement the `RecentCounter` class:

    - `RecentCounter()` Initializes the counter with zero recent requests.
    - `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that has happened in the past `3000` milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.

    It is **guaranteed** that every call to `ping` uses a strictly larger value of `t` than the previous call.

    ## Examples

    ```
    Input
    ["RecentCounter", "ping", "ping", "ping", "ping"]
    [[], [1], [100], [3001], [3002]]
    Output
    [null, 1, 2, 3, 3]

    Explanation
    RecentCounter recentCounter = new RecentCounter();
    recentCounter.ping(1); // requests = [1], range is [-2999,1], return 1
    recentCounter.ping(100); // requests = [1, 100], range is [-2900,100], return 2
    recentCounter.ping(3001); // requests = [1, 100, 3001], range is [1,3001], return 3
    recentCounter.ping(3002); // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
    ```

    ## Constraints

    - `1 <= t <= 10^9`
    - Each test case will call `ping` with **strictly increasing** values of `t`.
    - At most `10^4` calls will be made to `ping`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import deque

    class RecentCounter:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def ping(self, t: int) -> int:
            raise NotImplementedError('Implement ping')

    practice_exports = {'deque': deque, 'RecentCounter': RecentCounter}
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
