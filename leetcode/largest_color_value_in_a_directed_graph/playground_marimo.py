import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_path_value, run_largest_path_value
    from solution import Solution

    return Solution, assert_largest_path_value, run_largest_path_value


@app.cell
def _():
    # Example test case
    colors = "abaca"
    edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
    expected = 3
    return colors, edges, expected


@app.cell
def _(Solution, colors, edges, run_largest_path_value):
    result = run_largest_path_value(Solution, colors, edges)
    result
    return (result,)


@app.cell
def _(assert_largest_path_value, expected, result):
    assert_largest_path_value(result, expected)
    return


if __name__ == "__main__":
    app.run()
