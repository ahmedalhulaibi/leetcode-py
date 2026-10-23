import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_beauty, run_maximum_beauty
    from solution import Solution

    return Solution, assert_maximum_beauty, run_maximum_beauty


@app.cell
def _():
    # Example test case
    nums = [4, 6, 1, 2]
    k = 2
    expected = 3
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_maximum_beauty):
    result = run_maximum_beauty(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_maximum_beauty, expected, result):
    assert_maximum_beauty(result, expected)
    return


if __name__ == "__main__":
    app.run()
