import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_factors, run_get_factors
    from solution import Solution

    return Solution, assert_get_factors, run_get_factors


@app.cell
def _():
    # Example test case
    n = 12
    expected = [[2, 6], [3, 4], [2, 2, 3]]
    return expected, n


@app.cell
def _(Solution, n, run_get_factors):
    result = run_get_factors(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_get_factors, expected, result):
    assert_get_factors(result, expected)
    return


if __name__ == "__main__":
    app.run()
