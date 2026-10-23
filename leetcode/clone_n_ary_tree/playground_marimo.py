import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_clone_tree, run_clone_tree
    from solution import Solution

    return Solution, assert_clone_tree, run_clone_tree


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, None, 3, 2, 4, None, 5, 6]
    expected = [1, None, 3, 2, 4, None, 5, 6]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_clone_tree):
    result = run_clone_tree(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_clone_tree, expected, result):
    assert_clone_tree(result, expected)
    return


if __name__ == "__main__":
    app.run()
