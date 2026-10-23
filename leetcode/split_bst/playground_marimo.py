import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_split_bst, run_split_bst
    from solution import Solution

    return Solution, assert_split_bst, run_split_bst


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [4, 2, 6, 1, 3, 5, 7]
    target = 2
    expected_lists: list[list[int | None]] = [[2, 1], [4, 3, 6, None, None, 5, 7]]
    return expected_lists, root_list, target


@app.cell
def _(Solution, root_list: list[int | None], run_split_bst, target):
    result = run_split_bst(Solution, root_list, target)
    result
    return (result,)


@app.cell
def _(assert_split_bst, expected_lists: list[list[int | None]], result):
    assert_split_bst(result, expected_lists)
    return


if __name__ == "__main__":
    app.run()
