import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_interval, run_remove_interval
    from solution import Solution

    return Solution, assert_remove_interval, run_remove_interval


@app.cell
def _():
    # Example test case
    intervals = [[0, 2], [3, 4], [5, 7]]
    to_be_removed = [1, 6]
    expected = [[0, 1], [6, 7]]
    return expected, intervals, to_be_removed


@app.cell
def _(Solution, intervals, run_remove_interval, to_be_removed):
    result = run_remove_interval(Solution, intervals, to_be_removed)
    result
    return (result,)


@app.cell
def _(assert_remove_interval, expected, result):
    assert_remove_interval(result, expected)
    return


if __name__ == "__main__":
    app.run()
