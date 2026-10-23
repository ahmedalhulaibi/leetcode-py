import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_right_interval, run_find_right_interval
    from solution import Solution

    return Solution, assert_find_right_interval, run_find_right_interval


@app.cell
def _():
    # Example test case
    intervals = [[3, 4], [2, 3], [1, 2]]
    expected = [-1, 0, 1]
    return expected, intervals


@app.cell
def _(Solution, intervals, run_find_right_interval):
    result = run_find_right_interval(Solution, intervals)
    result
    return (result,)


@app.cell
def _(assert_find_right_interval, expected, result):
    assert_find_right_interval(result, expected)
    return


if __name__ == "__main__":
    app.run()
