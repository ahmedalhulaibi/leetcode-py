import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_tree_to_doubly_list, run_tree_to_doubly_list
    from solution import Solution

    return Solution, assert_tree_to_doubly_list, run_tree_to_doubly_list


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [4, 2, 5, 1, 3]
    expected_list = [1, 2, 3, 4, 5]
    return expected_list, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_tree_to_doubly_list):
    result = run_tree_to_doubly_list(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_tree_to_doubly_list, expected_list, result):
    assert_tree_to_doubly_list(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
