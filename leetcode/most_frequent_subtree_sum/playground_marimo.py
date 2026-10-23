import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_frequent_tree_sum, run_find_frequent_tree_sum
    from solution import Solution

    return Solution, assert_find_frequent_tree_sum, run_find_frequent_tree_sum


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [5, 2, -3]
    expected = [2, -3, 4]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_find_frequent_tree_sum):
    result = run_find_frequent_tree_sum(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_find_frequent_tree_sum, expected, result):
    assert_find_frequent_tree_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
