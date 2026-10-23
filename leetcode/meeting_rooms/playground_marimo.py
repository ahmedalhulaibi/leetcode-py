import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_attend_meetings, run_can_attend_meetings
    from solution import Solution

    return Solution, assert_can_attend_meetings, run_can_attend_meetings


@app.cell
def _():
    # Example test case
    intervals = [[0, 30], [5, 10], [15, 20]]
    expected = False
    return expected, intervals


@app.cell
def _(Solution, intervals, run_can_attend_meetings):
    result = run_can_attend_meetings(Solution, intervals)
    result
    return (result,)


@app.cell
def _(assert_can_attend_meetings, expected, result):
    assert_can_attend_meetings(result, expected)
    return


if __name__ == "__main__":
    app.run()
