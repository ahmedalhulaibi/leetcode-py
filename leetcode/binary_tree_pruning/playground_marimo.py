import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_prune_tree, run_prune_tree
    from solution import Solution

    return Solution, assert_prune_tree, run_prune_tree


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, None, 0, 0, 1]
    expected_list: list[int | None] = [1, None, 0, None, 1]
    return expected_list, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_prune_tree):
    result = run_prune_tree(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_prune_tree, expected_list: list[int | None], result):
    assert_prune_tree(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
