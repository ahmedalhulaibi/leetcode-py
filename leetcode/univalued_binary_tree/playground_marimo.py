import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_unival_tree, run_is_unival_tree
    from solution import Solution

    return Solution, assert_is_unival_tree, run_is_unival_tree


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 1, 1, 1, 1, None, 1]
    expected: bool = True
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_is_unival_tree):
    result = run_is_unival_tree(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_is_unival_tree, expected: bool, result):
    assert_is_unival_tree(result, expected)
    return


if __name__ == "__main__":
    app.run()
