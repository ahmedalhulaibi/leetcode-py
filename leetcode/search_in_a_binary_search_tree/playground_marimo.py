import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_search_bst, run_search_bst
    from solution import Solution

    return Solution, assert_search_bst, run_search_bst


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [4, 2, 7, 1, 3]
    val = 2
    expected_list: list[int | None] = [2, 1, 3]
    return expected_list, root_list, val


@app.cell
def _(Solution, root_list: list[int | None], run_search_bst, val):
    result = run_search_bst(Solution, root_list, val)
    result
    return (result,)


@app.cell
def _(assert_search_bst, expected_list: list[int | None], result):
    assert_search_bst(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
