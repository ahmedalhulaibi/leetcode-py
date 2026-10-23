import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_combine, run_combine
    from solution import Solution

    return Solution, assert_combine, run_combine


@app.cell
def _():
    # Example test case
    n = 4
    k = 2
    expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    return expected, k, n


@app.cell
def _(Solution, k, n, run_combine):
    result = run_combine(Solution, n, k)
    result
    return (result,)


@app.cell
def _(assert_combine, expected, result):
    assert_combine(result, expected)
    return


if __name__ == "__main__":
    app.run()
