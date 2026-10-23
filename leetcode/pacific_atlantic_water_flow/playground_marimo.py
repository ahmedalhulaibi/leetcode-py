import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_pacific_atlantic, run_pacific_atlantic
    from solution import Solution

    return Solution, assert_pacific_atlantic, run_pacific_atlantic


@app.cell
def _():
    # Example test case
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    return expected, heights


@app.cell
def _(Solution, heights, run_pacific_atlantic):
    result = run_pacific_atlantic(Solution, heights)
    result
    return (result,)


@app.cell
def _(assert_pacific_atlantic, expected, result):
    assert_pacific_atlantic(result, expected)
    return


if __name__ == "__main__":
    app.run()
