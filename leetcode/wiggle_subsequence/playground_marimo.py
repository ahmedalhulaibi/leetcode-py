import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_wiggle_max_length, run_wiggle_max_length
    from solution import Solution

    return Solution, assert_wiggle_max_length, run_wiggle_max_length


@app.cell
def _():
    # Example test case
    nums: list[int] = [1, 7, 4, 9, 2, 5]
    expected = 6
    return expected, nums


@app.cell
def _(Solution, nums: list[int], run_wiggle_max_length):
    result = run_wiggle_max_length(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_wiggle_max_length, expected, result):
    assert_wiggle_max_length(result, expected)
    return


if __name__ == "__main__":
    app.run()
