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
    # 729. My Calendar I

    **Medium** · Array, Binary Search, Design, Segment Tree, Ordered Set

    You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a **double booking**.

    A **double booking** happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

    The event can be represented as a pair of integers `startTime` and `endTime` that represents a booking on the half-open interval `[startTime, endTime)`, the range of real numbers `x` such that `startTime <= x < endTime`.

    Implement the `MyCalendar` class:

    - `MyCalendar()` Initializes the calendar object.
    - `boolean book(int startTime, int endTime)` Returns `true` if the event can be added to the calendar successfully without causing a **double booking**. Otherwise, return `false` and do not add the event to the calendar.

    ## Examples

    ```
    Input
    ["MyCalendar", "book", "book", "book"]
    [[], [10, 20], [15, 25], [20, 30]]
    Output
    [null, true, false, true]

    Explanation
    MyCalendar myCalendar = new MyCalendar();
    myCalendar.book(10, 20); // return True
    myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
    myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
    ```

    ## Constraints

    - 0 <= start < end <= 10^9
    - At most 1000 calls will be made to book.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MyCalendar:

        def __init__(self):
            raise NotImplementedError('Implement __init__')

        def book(self, start: int, end: int) -> bool:
            raise NotImplementedError('Implement book')

    practice_exports = {'MyCalendar': MyCalendar}
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
