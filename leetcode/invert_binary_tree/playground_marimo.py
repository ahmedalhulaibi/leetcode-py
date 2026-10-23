import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_invert_tree, run_invert_tree
    from solution import Solution

    return Solution, assert_invert_tree, run_invert_tree


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [4, 2, 7, 1, 3, 6, 9]
    expected_list: list[int | None] = [4, 7, 2, 9, 6, 3, 1]
    return expected_list, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_invert_tree):
    result = run_invert_tree(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_invert_tree, expected_list: list[int | None], result):
    assert_invert_tree(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
