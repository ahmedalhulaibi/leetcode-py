import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_orders, run_count_orders
    from solution import Solution

    return Solution, assert_count_orders, run_count_orders


@app.cell
def _():
    # Example test case
    n = 3
    expected = 90
    return expected, n


@app.cell
def _(Solution, n, run_count_orders):
    result = run_count_orders(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_count_orders, expected, result):
    assert_count_orders(result, expected)
    return


if __name__ == "__main__":
    app.run()
