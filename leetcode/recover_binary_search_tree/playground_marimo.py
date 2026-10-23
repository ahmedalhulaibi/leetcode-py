import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_recover_tree, run_recover_tree
    from solution import Solution

    return Solution, assert_recover_tree, run_recover_tree


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 3, None, None, 2]
    expected_list: list[int | None] = [3, 1, None, None, 2]
    return expected_list, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_recover_tree):
    result = run_recover_tree(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_recover_tree, expected_list: list[int | None], result):
    assert_recover_tree(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
