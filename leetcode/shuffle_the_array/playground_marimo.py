import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shuffle, run_shuffle
    from solution import Solution

    return Solution, assert_shuffle, run_shuffle


@app.cell
def _():
    # Example test case
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    expected = [2, 3, 5, 4, 1, 7]
    return expected, n, nums


@app.cell
def _(Solution, n, nums, run_shuffle):
    result = run_shuffle(Solution, nums, n)
    result
    return (result,)


@app.cell
def _(assert_shuffle, expected, result):
    assert_shuffle(result, expected)
    return


if __name__ == "__main__":
    app.run()
