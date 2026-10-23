import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_index, run_minimum_index
    from solution import Solution

    return Solution, assert_minimum_index, run_minimum_index


@app.cell
def _():
    # Example test case
    nums = [1, 2, 2, 2]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums, run_minimum_index):
    result = run_minimum_index(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_minimum_index, expected, result):
    assert_minimum_index(result, expected)
    return


if __name__ == "__main__":
    app.run()
