import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_meeting_rooms, run_min_meeting_rooms
    from solution import Solution

    return Solution, assert_min_meeting_rooms, run_min_meeting_rooms


@app.cell
def _():
    # Example test case
    intervals = [[0, 30], [5, 10], [15, 20]]
    expected = 2
    return expected, intervals


@app.cell
def _(Solution, intervals, run_min_meeting_rooms):
    result = run_min_meeting_rooms(Solution, intervals)
    result
    return (result,)


@app.cell
def _(assert_min_meeting_rooms, expected, result):
    assert_min_meeting_rooms(result, expected)
    return


if __name__ == "__main__":
    app.run()
