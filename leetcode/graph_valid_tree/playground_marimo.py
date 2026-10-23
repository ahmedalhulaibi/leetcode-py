import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_valid_tree, run_valid_tree
    from solution import Solution

    return Solution, assert_valid_tree, run_valid_tree


@app.cell
def _():
    # Example test case
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    expected = True
    return edges, expected, n


@app.cell
def _(Solution, edges, n, run_valid_tree):
    result = run_valid_tree(Solution, n, edges)
    result
    return (result,)


@app.cell
def _(assert_valid_tree, expected, result):
    assert_valid_tree(result, expected)
    return


if __name__ == "__main__":
    app.run()
