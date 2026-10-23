import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_sum_min_product, run_max_sum_min_product
    from solution import Solution

    return Solution, assert_max_sum_min_product, run_max_sum_min_product


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 2]
    expected = 14
    return expected, nums


@app.cell
def _(Solution, nums, run_max_sum_min_product):
    result = run_max_sum_min_product(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_max_sum_min_product, expected, result):
    assert_max_sum_min_product(result, expected)
    return


if __name__ == "__main__":
    app.run()
