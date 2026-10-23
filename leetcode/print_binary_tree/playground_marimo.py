import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_print_tree, run_print_tree
    from solution import Solution

    return Solution, assert_print_tree, run_print_tree


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2]
    expected = [["", "1", ""], ["2", "", ""]]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_print_tree):
    result = run_print_tree(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_print_tree, expected, result):
    assert_print_tree(result, expected)
    return


if __name__ == "__main__":
    app.run()
