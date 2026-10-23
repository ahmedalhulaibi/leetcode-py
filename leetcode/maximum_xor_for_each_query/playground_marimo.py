import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_maximum_xor, run_get_maximum_xor
    from solution import Solution

    return Solution, assert_get_maximum_xor, run_get_maximum_xor


@app.cell
def _():
    # Example test case
    nums = [0, 1, 1, 3]
    maximum_bit = 2
    expected = [0, 3, 2, 3]
    return expected, maximum_bit, nums


@app.cell
def _(Solution, maximum_bit, nums, run_get_maximum_xor):
    result = run_get_maximum_xor(Solution, nums, maximum_bit)
    result
    return (result,)


@app.cell
def _(assert_get_maximum_xor, expected, result):
    assert_get_maximum_xor(result, expected)
    return


if __name__ == "__main__":
    app.run()
