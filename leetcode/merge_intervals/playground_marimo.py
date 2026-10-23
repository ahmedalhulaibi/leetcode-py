import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_merge, run_merge
    from solution import Solution

    return Solution, assert_merge, run_merge


@app.cell
def _():
    # Example test case
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected = [[1, 6], [8, 10], [15, 18]]
    return expected, intervals


@app.cell
def _(Solution, intervals, run_merge):
    result = run_merge(Solution, intervals)
    result
    return (result,)


@app.cell
def _(assert_merge, expected, result):
    assert_merge(result, expected)
    return


if __name__ == "__main__":
    app.run()
