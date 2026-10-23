import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_interval, run_min_interval
    from solution import Solution

    return Solution, assert_min_interval, run_min_interval


@app.cell
def _():
    # Example test case
    intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
    queries = [2, 3, 4, 5]
    expected = [3, 3, 1, 4]
    return expected, intervals, queries


@app.cell
def _(Solution, intervals, queries, run_min_interval):
    result = run_min_interval(Solution, intervals, queries)
    result
    return (result,)


@app.cell
def _(assert_min_interval, expected, result):
    assert_min_interval(result, expected)
    return


if __name__ == "__main__":
    app.run()
