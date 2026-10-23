import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_valid_bst, run_is_valid_bst
    from solution import Solution

    return Solution, assert_is_valid_bst, run_is_valid_bst


@app.cell
def _():
    # Example test case
    root_list = [2, 1, 3]
    expected = True
    return expected, root_list


@app.cell
def _(Solution, root_list, run_is_valid_bst):
    result = run_is_valid_bst(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_is_valid_bst, expected, result):
    assert_is_valid_bst(result, expected)
    return


if __name__ == "__main__":
    app.run()
