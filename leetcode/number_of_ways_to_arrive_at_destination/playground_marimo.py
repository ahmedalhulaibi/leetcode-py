import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_paths, run_count_paths
    from solution import Solution

    return Solution, assert_count_paths, run_count_paths


@app.cell
def _():
    # Example test case
    n = 7
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1]]
    expected = 4
    return expected, n, roads


@app.cell
def _(Solution, n, roads, run_count_paths):
    result = run_count_paths(Solution, n, roads)
    result
    return (result,)


@app.cell
def _(assert_count_paths, expected, result):
    assert_count_paths(result, expected)
    return


if __name__ == "__main__":
    app.run()
