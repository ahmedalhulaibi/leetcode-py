import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_maximum_xor, run_find_maximum_xor
    from solution import Solution

    return Solution, assert_find_maximum_xor, run_find_maximum_xor


@app.cell
def _():
    # Example test case
    nums = [3, 10, 5, 25, 2, 8]
    expected = 28
    return expected, nums


@app.cell
def _(Solution, nums, run_find_maximum_xor):
    result = run_find_maximum_xor(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_maximum_xor, expected, result):
    assert_find_maximum_xor(result, expected)
    return


if __name__ == "__main__":
    app.run()
