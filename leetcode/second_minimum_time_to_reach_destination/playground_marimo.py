import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_second_minimum, run_second_minimum
    from solution import Solution

    return Solution, assert_second_minimum, run_second_minimum


@app.cell
def _():
    # Example test case
    n = 5
    edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
    time = 3
    change = 5
    expected = 13
    return change, edges, expected, n, time


@app.cell
def _(Solution, change, edges, n, run_second_minimum, time):
    result = run_second_minimum(Solution, n, edges, time, change)
    result
    return (result,)


@app.cell
def _(assert_second_minimum, expected, result):
    assert_second_minimum(result, expected)
    return


if __name__ == "__main__":
    app.run()
