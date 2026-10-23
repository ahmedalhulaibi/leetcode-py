import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_count, run_max_count
    from solution import Solution

    return Solution, assert_max_count, run_max_count


@app.cell
def _():
    # Example test case
    m = 3
    n = 3
    ops = [[2, 2], [3, 3]]
    expected = 4
    return expected, m, n, ops


@app.cell
def _(Solution, m, n, ops, run_max_count):
    result = run_max_count(Solution, m, n, ops)
    result
    return (result,)


@app.cell
def _(assert_max_count, expected, result):
    assert_max_count(result, expected)
    return


if __name__ == "__main__":
    app.run()
