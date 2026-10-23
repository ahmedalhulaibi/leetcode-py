import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_range_sum_bst, run_range_sum_bst
    from solution import Solution

    return Solution, assert_range_sum_bst, run_range_sum_bst


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [10, 5, 15, 3, 7, None, 18]
    low = 7
    high = 15
    expected = 32
    return expected, high, low, root_list


@app.cell
def _(Solution, high, low, root_list: list[int | None], run_range_sum_bst):
    result = run_range_sum_bst(Solution, root_list, low, high)
    result
    return (result,)


@app.cell
def _(assert_range_sum_bst, expected, result):
    assert_range_sum_bst(result, expected)
    return


if __name__ == "__main__":
    app.run()
