import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sorted_array_to_bst, run_sorted_array_to_bst
    from solution import Solution

    return Solution, assert_sorted_array_to_bst, run_sorted_array_to_bst


@app.cell
def _():
    # Example test case
    nums = [-10, -3, 0, 5, 9]
    return (nums,)


@app.cell
def _(Solution, nums, run_sorted_array_to_bst):
    result = run_sorted_array_to_bst(Solution, nums)
    result.to_list() if result else []
    return (result,)


@app.cell
def _(assert_sorted_array_to_bst, nums, result):
    assert_sorted_array_to_bst(result, nums)
    return


if __name__ == "__main__":
    app.run()
