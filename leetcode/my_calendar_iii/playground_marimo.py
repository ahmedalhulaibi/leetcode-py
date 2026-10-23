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
    # 732. My Calendar III

    **Hard** · Binary Search, Design, Segment Tree, Prefix Sum, Ordered Set

    A `k`-booking happens when `k` events have some non-empty intersection (i.e., there is some time that is common to all `k` events.)

    You are given some events `[startTime, endTime)`, after each given event, return an integer `k` representing the maximum `k`-booking between all the previous events.

    Implement the `MyCalendarThree` class:

    - `MyCalendarThree()` Initializes the object.
    - `int book(int startTime, int endTime)` Returns an integer `k` representing the largest integer such that there exists a `k`-booking in the calendar.

    ## Examples

    ```
    Input
    ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
    [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    Output
    [null, 1, 1, 2, 3, 3, 3]

    Explanation
    MyCalendarThree myCalendarThree = new MyCalendarThree();
    myCalendarThree.book(10, 20); // return 1
    myCalendarThree.book(50, 60); // return 1
    myCalendarThree.book(10, 40); // return 2
    myCalendarThree.book(5, 15);  // return 3
    myCalendarThree.book(5, 10);  // return 3
    myCalendarThree.book(25, 55); // return 3
    ```

    ## Constraints

    - 0 <= startTime < endTime <= 10^9
    - At most 400 calls will be made to book.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class MyCalendarThree:

        def __init__(self) -> None:
            raise NotImplementedError('Implement __init__')

        def book(self, start_time: int, end_time: int) -> int:
            raise NotImplementedError('Implement book')

    practice_exports = {'MyCalendarThree': MyCalendarThree}
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
