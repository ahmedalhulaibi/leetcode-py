import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_total_money, run_total_money
    from solution import Solution

    return Solution, assert_total_money, run_total_money


@app.cell
def _():
    # Example test case
    n = 4
    expected = 10
    return expected, n


@app.cell
def _(Solution, n, run_total_money):
    result = run_total_money(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_total_money, expected, result):
    assert_total_money(result, expected)
    return


if __name__ == "__main__":
    app.run()
