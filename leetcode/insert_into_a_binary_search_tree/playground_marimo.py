import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_insert_into_bst, run_insert_into_bst
    from solution import Solution

    return Solution, assert_insert_into_bst, run_insert_into_bst


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [4, 2, 7, 1, 3]
    val = 5
    expected = [1, 2, 3, 4, 5, 7]
    return expected, root_list, val


@app.cell
def _(Solution, root_list: list[int | None], run_insert_into_bst, val):
    result = run_insert_into_bst(Solution, root_list, val)
    result
    return (result,)


@app.cell
def _(assert_insert_into_bst, expected, result):
    assert_insert_into_bst(result, expected)
    return


if __name__ == "__main__":
    app.run()
