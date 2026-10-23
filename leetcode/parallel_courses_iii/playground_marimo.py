import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_time, run_minimum_time
    from solution import Solution

    return Solution, assert_minimum_time, run_minimum_time


@app.cell
def _():
    # Example test case
    n = 3
    relations = [[1, 3], [2, 3]]
    time = [3, 2, 5]
    expected = 8
    return expected, n, relations, time


@app.cell
def _(Solution, n, relations, run_minimum_time, time):
    result = run_minimum_time(Solution, n, relations, time)
    result
    return (result,)


@app.cell
def _(assert_minimum_time, expected, result):
    assert_minimum_time(result, expected)
    return


if __name__ == "__main__":
    app.run()
