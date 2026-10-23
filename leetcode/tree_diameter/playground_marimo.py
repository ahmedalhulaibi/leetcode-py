import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_tree_diameter, run_tree_diameter
    from solution import Solution

    return Solution, assert_tree_diameter, run_tree_diameter


@app.cell
def _():
    # Example test case
    edges: list[list[int]] = [[0, 1], [0, 2]]
    expected = 2
    return edges, expected


@app.cell
def _(Solution, edges: list[list[int]], run_tree_diameter):
    result = run_tree_diameter(Solution, edges)
    result
    return (result,)


@app.cell
def _(assert_tree_diameter, expected, result):
    assert_tree_diameter(result, expected)
    return


if __name__ == "__main__":
    app.run()
