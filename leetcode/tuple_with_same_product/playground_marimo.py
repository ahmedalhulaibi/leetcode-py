import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_tuple_same_product, run_tuple_same_product
    from solution import Solution

    return Solution, assert_tuple_same_product, run_tuple_same_product


@app.cell
def _():
    # Example test case
    nums = [2, 3, 4, 6]
    expected = 8
    return expected, nums


@app.cell
def _(Solution, nums, run_tuple_same_product):
    result = run_tuple_same_product(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_tuple_same_product, expected, result):
    assert_tuple_same_product(result, expected)
    return


if __name__ == "__main__":
    app.run()
