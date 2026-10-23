import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_number_of_good_paths, run_number_of_good_paths
    from solution import Solution

    return Solution, assert_number_of_good_paths, run_number_of_good_paths


@app.cell
def _():
    # Example test case
    vals = [1, 3, 2, 1, 3]
    edges = [[0, 1], [0, 2], [2, 3], [2, 4]]
    expected = 6
    return edges, expected, vals


@app.cell
def _(Solution, edges, run_number_of_good_paths, vals):
    result = run_number_of_good_paths(Solution, vals, edges)
    result
    return (result,)


@app.cell
def _(assert_number_of_good_paths, expected, result):
    assert_number_of_good_paths(result, expected)
    return


if __name__ == "__main__":
    app.run()
