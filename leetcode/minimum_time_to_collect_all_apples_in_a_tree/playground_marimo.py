import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_time, run_min_time
    from solution import Solution

    return Solution, assert_min_time, run_min_time


@app.cell
def _():
    # Example test case
    n = 7
    edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    has_apple = [False, False, True, False, True, True, False]
    expected = 8
    return edges, expected, has_apple, n


@app.cell
def _(Solution, edges, has_apple, n, run_min_time):
    result = run_min_time(Solution, n, edges, has_apple)
    result
    return (result,)


@app.cell
def _(assert_min_time, expected, result):
    assert_min_time(result, expected)
    return


if __name__ == "__main__":
    app.run()
