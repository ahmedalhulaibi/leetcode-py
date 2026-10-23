import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_check_equal_tree, run_check_equal_tree
    from solution import Solution

    return Solution, assert_check_equal_tree, run_check_equal_tree


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [5, 10, 10, None, None, 2, 3]
    expected = True
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_check_equal_tree):
    result = run_check_equal_tree(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_check_equal_tree, expected, result):
    assert_check_equal_tree(result, expected)
    return


if __name__ == "__main__":
    app.run()
