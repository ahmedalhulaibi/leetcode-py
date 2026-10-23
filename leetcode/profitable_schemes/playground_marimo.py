import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_profitable_schemes, run_profitable_schemes
    from solution import Solution

    return Solution, assert_profitable_schemes, run_profitable_schemes


@app.cell
def _():
    # Example test case
    n = 5
    min_profit = 3
    group = [2, 2]
    profit = [2, 3]
    expected = 2
    return expected, group, min_profit, n, profit


@app.cell
def _(Solution, group, min_profit, n, profit, run_profitable_schemes):
    result = run_profitable_schemes(Solution, n, min_profit, group, profit)
    result
    return (result,)


@app.cell
def _(assert_profitable_schemes, expected, result):
    assert_profitable_schemes(result, expected)
    return


if __name__ == "__main__":
    app.run()
