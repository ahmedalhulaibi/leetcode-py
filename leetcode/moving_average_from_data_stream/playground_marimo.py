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
    # 346. Moving Average from Data Stream

    **Easy** · Design, Queue, Array, Data Stream

    Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

    Implement the `MovingAverage` class:

    - `MovingAverage(int size)` Initializes the object with the size of the window `size`.
    - `double next(int val)` Returns the moving average of the last `size` values of the stream.

    ## Examples

    ```
    Input
    ["MovingAverage", "next", "next", "next", "next"]
    [[3], [1], [10], [3], [5]]
    Output
    [null, 1.0, 5.5, 4.66667, 6.0]

    Explanation
    MovingAverage movingAverage = new MovingAverage(3);
    movingAverage.next(1); // return 1.0 = 1 / 1
    movingAverage.next(10); // return 5.5 = (1 + 10) / 2
    movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
    movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
    ```

    ## Constraints

    - `1 <= size <= 1000`
    - `-10^5 <= val <= 10^5`
    - At most `10^4` calls will be made to `next`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import deque

    class MovingAverage:

        def __init__(self, size: int) -> None:
            raise NotImplementedError('Implement __init__')

        def next(self, val: int) -> float:
            raise NotImplementedError('Implement next')

    practice_exports = {'deque': deque, 'MovingAverage': MovingAverage}
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
