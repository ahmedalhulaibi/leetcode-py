import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_most_booked, run_most_booked
    from solution import Solution

    return Solution, assert_most_booked, run_most_booked


@app.cell
def _():
    # Example test case
    n = 2
    meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
    expected = 0
    return expected, meetings, n


@app.cell
def _(Solution, meetings, n, run_most_booked):
    result = run_most_booked(Solution, n, meetings)
    result
    return (result,)


@app.cell
def _(assert_most_booked, expected, result):
    assert_most_booked(result, expected)
    return


if __name__ == "__main__":
    app.run()
