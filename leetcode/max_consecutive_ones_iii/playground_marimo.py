import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_ones, run_longest_ones
    from solution import Solution

    return Solution, assert_longest_ones, run_longest_ones


@app.cell
def _():
    # Example test case
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    expected = 6
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_longest_ones):
    result = run_longest_ones(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_longest_ones, expected, result):
    assert_longest_ones(result, expected)
    return


if __name__ == "__main__":
    app.run()
