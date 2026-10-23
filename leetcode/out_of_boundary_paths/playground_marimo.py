import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_paths, run_find_paths
    from solution import Solution

    return Solution, assert_find_paths, run_find_paths


@app.cell
def _():
    # Example test case
    m = 2
    n = 2
    max_move = 2
    start_row = 0
    start_column = 0
    expected = 6
    return expected, m, max_move, n, start_column, start_row


@app.cell
def _(Solution, m, max_move, n, run_find_paths, start_column, start_row):
    result = run_find_paths(Solution, m, n, max_move, start_row, start_column)
    result
    return (result,)


@app.cell
def _(assert_find_paths, expected, result):
    assert_find_paths(result, expected)
    return


if __name__ == "__main__":
    app.run()
