import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_product_difference, run_max_product_difference
    from solution import Solution

    return Solution, assert_max_product_difference, run_max_product_difference


@app.cell
def _():
    # Example test case
    nums = [5, 6, 2, 7, 4]
    expected = 34
    return expected, nums


@app.cell
def _(Solution, nums, run_max_product_difference):
    result = run_max_product_difference(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_max_product_difference, expected, result):
    assert_max_product_difference(result, expected)
    return


if __name__ == "__main__":
    app.run()
