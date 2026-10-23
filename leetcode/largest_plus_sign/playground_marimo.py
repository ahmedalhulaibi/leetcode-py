import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_order_of_largest_plus_sign, run_order_of_largest_plus_sign
    from solution import Solution

    return (
        Solution,
        assert_order_of_largest_plus_sign,
        run_order_of_largest_plus_sign,
    )


@app.cell
def _():
    # Example test case
    n = 5
    mines = [[4, 2]]
    expected = 2
    return expected, mines, n


@app.cell
def _(Solution, mines, n, run_order_of_largest_plus_sign):
    result = run_order_of_largest_plus_sign(Solution, n, mines)
    result
    return (result,)


@app.cell
def _(assert_order_of_largest_plus_sign, expected, result):
    assert_order_of_largest_plus_sign(result, expected)
    return


if __name__ == "__main__":
    app.run()
