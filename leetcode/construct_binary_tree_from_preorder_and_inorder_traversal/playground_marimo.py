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
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    expected_list = [3, 9, 20, None, None, 15, 7]
    return expected_list, inorder, preorder


@app.cell
def _(Solution, inorder, preorder, run_build_tree):
    result = run_build_tree(Solution, preorder, inorder)
    result
    return (result,)


@app.cell
def _(assert_build_tree, expected_list, result):
    assert_build_tree(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
