import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_consecutive, run_longest_consecutive
    from solution import Solution

    return Solution, assert_longest_consecutive, run_longest_consecutive


@app.cell
def _():
    # Example test case
    nums = [100, 4, 200, 1, 3, 2]
    expected = 4
    return expected, nums


@app.cell
def _(Solution, nums, run_longest_consecutive):
    result = run_longest_consecutive(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_longest_consecutive, expected, result):
    assert_longest_consecutive(result, expected)
    return


if __name__ == "__main__":
    app.run()
