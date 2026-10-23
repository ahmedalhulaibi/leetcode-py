import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_product, run_maximum_product
    from solution import Solution

    return Solution, assert_maximum_product, run_maximum_product


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 4]
    expected = 24
    return expected, nums


@app.cell
def _(Solution, nums, run_maximum_product):
    result = run_maximum_product(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_maximum_product, expected, result):
    assert_maximum_product(result, expected)
    return


if __name__ == "__main__":
    app.run()
