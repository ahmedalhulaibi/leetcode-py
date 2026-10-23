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
    # 731. My Calendar II

    **Medium** · Array, Binary Search, Design, Segment Tree, Ordered Set, Prefix Sum

    You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

    A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

    The event can be represented as a pair of integers `startTime` and `endTime` that represents a booking on the half-open interval `[startTime, endTime)`, the range of real numbers `x` such that `startTime <= x < endTime`.

    Implement the `MyCalendarTwo` class:

    - `MyCalendarTwo()` Initializes the calendar object.
    - `boolean book(int startTime, int endTime)` Returns `true` if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return `false` and do not add the event to the calendar.

    ## Examples

    ```
    Input
    ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
    [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    Output
    [null, true, true, true, false, true, true]

    Explanation
    MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
    myCalendarTwo.book(10, 20); // return True, The event can be booked.
    myCalendarTwo.book(50, 60); // return True, The event can be booked.
    myCalendarTwo.book(10, 40); // return True, The event can be double booked.
    myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
    myCalendarTwo.book(5, 10);  // return True, The event can be booked, as it does not use time 10 which is already double booked.
    myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event;
                                // the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
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
    class MyCalendarTwo:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def book(self, start_time: int, end_time: int) -> bool:
            raise NotImplementedError('Implement book')

    practice_exports = {'MyCalendarTwo': MyCalendarTwo}
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
