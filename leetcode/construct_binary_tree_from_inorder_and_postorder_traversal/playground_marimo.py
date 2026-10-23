import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_build_tree, run_build_tree
    from solution import Solution

    return Solution, assert_build_tree, run_build_tree


@app.cell
def _():
    # Example test case
    inorder: list[int] = [9, 3, 15, 20, 7]
    postorder: list[int] = [9, 15, 7, 20, 3]
    expected_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
    return expected_list, inorder, postorder


@app.cell
def _(Solution, inorder: list[int], postorder: list[int], run_build_tree):
    result = run_build_tree(Solution, inorder, postorder)
    result
    return (result,)


@app.cell
def _(assert_build_tree, expected_list: list[int | None], result):
    assert_build_tree(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
