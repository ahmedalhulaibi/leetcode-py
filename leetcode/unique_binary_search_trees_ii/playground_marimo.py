import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_generate_trees, run_generate_trees
    from solution import Solution

    return Solution, assert_generate_trees, run_generate_trees


@app.cell
def _():
    # Example test case
    n = 3
    expected_tree: list[int | None] = [2, 1, 3]
    return expected_tree, n


@app.cell
def _(Solution, n, run_generate_trees):
    result = run_generate_trees(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_generate_trees, expected_tree: list[int | None], n, result):
    assert_generate_trees(result, n, expected_tree)
    return


if __name__ == "__main__":
    app.run()
