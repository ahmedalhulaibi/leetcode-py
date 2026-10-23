import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_inorder_traversal, run_inorder_traversal
    from solution import Solution

    return Solution, assert_inorder_traversal, run_inorder_traversal


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, None, 2, None, None, 3]
    expected = [1, 3, 2]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_inorder_traversal):
    result = run_inorder_traversal(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_inorder_traversal, expected, result):
    assert_inorder_traversal(result, expected)
    return


if __name__ == "__main__":
    app.run()
