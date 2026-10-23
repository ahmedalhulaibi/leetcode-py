import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sorted_list_to_bst, run_sorted_list_to_bst
    from solution import Solution

    return Solution, assert_sorted_list_to_bst, run_sorted_list_to_bst


@app.cell
def _():
    # Example test case
    head_vals = [-10, -3, 0, 5, 9]
    return (head_vals,)


@app.cell
def _(Solution, head_vals, run_sorted_list_to_bst):
    result = run_sorted_list_to_bst(Solution, head_vals)
    result.to_list() if result else []
    return (result,)


@app.cell
def _(assert_sorted_list_to_bst, head_vals, result):
    assert_sorted_list_to_bst(result, head_vals)
    return


if __name__ == "__main__":
    app.run()
