import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_insert_into_max_tree, run_insert_into_max_tree
    from solution import Solution

    return Solution, assert_insert_into_max_tree, run_insert_into_max_tree


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [4, 1, 3, None, None, 2]
    val = 5
    expected_list: list[int | None] = [5, 4, None, 1, 3, None, None, 2]
    return expected_list, root_list, val


@app.cell
def _(Solution, root_list: list[int | None], run_insert_into_max_tree, val):
    result = run_insert_into_max_tree(Solution, root_list, val)
    result
    return (result,)


@app.cell
def _(assert_insert_into_max_tree, expected_list: list[int | None], result):
    assert_insert_into_max_tree(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
