import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_product_except_self, run_product_except_self
    from solution import Solution

    return Solution, assert_product_except_self, run_product_except_self


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    return expected, nums


@app.cell
def _(Solution, nums, run_product_except_self):
    result = run_product_except_self(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_product_except_self, expected, result):
    assert_product_except_self(result, expected)
    return


if __name__ == "__main__":
    app.run()
