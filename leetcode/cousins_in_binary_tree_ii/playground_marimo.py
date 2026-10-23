import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_replace_value_in_tree, run_replace_value_in_tree
    from solution import Solution

    return Solution, assert_replace_value_in_tree, run_replace_value_in_tree


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [5, 4, 9, 1, 10, None, 7]
    expected_list: list[int | None] = [0, 0, 0, 7, 7, None, 11]
    return expected_list, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_replace_value_in_tree):
    result = run_replace_value_in_tree(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_replace_value_in_tree, expected_list: list[int | None], result):
    assert_replace_value_in_tree(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
