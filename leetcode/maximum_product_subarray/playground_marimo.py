import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_product, run_max_product
    from solution import Solution

    return Solution, assert_max_product, run_max_product


@app.cell
def _():
    # Example test case
    nums = [2, 3, -2, 4]
    expected = 6
    return expected, nums


@app.cell
def _(Solution, nums, run_max_product):
    result = run_max_product(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_max_product, expected, result):
    assert_max_product(result, expected)
    return


if __name__ == "__main__":
    app.run()
