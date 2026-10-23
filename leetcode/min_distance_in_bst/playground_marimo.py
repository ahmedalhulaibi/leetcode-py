import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_diff_in_bst, run_min_diff_in_bst
    from solution import Solution

    return Solution, assert_min_diff_in_bst, run_min_diff_in_bst


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [4, 2, 6, 1, 3]
    expected = 1
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_min_diff_in_bst):
    result = run_min_diff_in_bst(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_min_diff_in_bst, expected, result):
    assert_min_diff_in_bst(result, expected)
    return


if __name__ == "__main__":
    app.run()
