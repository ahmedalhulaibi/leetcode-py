import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_max_length, run_find_max_length
    from solution import Solution

    return Solution, assert_find_max_length, run_find_max_length


@app.cell
def _():
    # Example test case
    nums = [0, 1]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums, run_find_max_length):
    result = run_find_max_length(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_max_length, expected, result):
    assert_find_max_length(result, expected)
    return


if __name__ == "__main__":
    app.run()
