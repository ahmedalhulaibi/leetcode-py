import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_min_height_trees, run_find_min_height_trees
    from solution import Solution

    return Solution, assert_find_min_height_trees, run_find_min_height_trees


@app.cell
def _():
    # Example test case
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    expected = [1]
    return edges, expected, n


@app.cell
def _(Solution, edges, n, run_find_min_height_trees):
    result = run_find_min_height_trees(Solution, n, edges)
    result
    return (result,)


@app.cell
def _(assert_find_min_height_trees, expected, result):
    assert_find_min_height_trees(result, expected)
    return


if __name__ == "__main__":
    app.run()
