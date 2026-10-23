import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_preorder, run_preorder
    from solution import Solution

    return Solution, assert_preorder, run_preorder


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, None, 3, 2, 4, None, 5, 6]
    expected = [1, 3, 5, 6, 2, 4]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_preorder):
    result = run_preorder(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_preorder, expected, result):
    assert_preorder(result, expected)
    return


if __name__ == "__main__":
    app.run()
