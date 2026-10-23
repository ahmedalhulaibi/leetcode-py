import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_insert, run_insert
    from solution import Solution

    return Solution, assert_insert, run_insert


@app.cell
def _():
    # Example test case
    intervals = [[1, 3], [6, 9]]
    new_interval = [2, 5]
    expected = [[1, 5], [6, 9]]
    return expected, intervals, new_interval


@app.cell
def _(Solution, intervals, new_interval, run_insert):
    result = run_insert(Solution, intervals, new_interval)
    result
    return (result,)


@app.cell
def _(assert_insert, expected, result):
    assert_insert(result, expected)
    return


if __name__ == "__main__":
    app.run()
