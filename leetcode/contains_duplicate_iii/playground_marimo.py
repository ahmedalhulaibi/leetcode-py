import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_contains_nearby_almost_duplicate, run_contains_nearby_almost_duplicate
    from solution import Solution

    return (
        Solution,
        assert_contains_nearby_almost_duplicate,
        run_contains_nearby_almost_duplicate,
    )


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 1]
    index_diff = 3
    value_diff = 0
    expected = True
    return expected, index_diff, nums, value_diff


@app.cell
def _(
    Solution,
    index_diff,
    nums,
    run_contains_nearby_almost_duplicate,
    value_diff,
):
    result = run_contains_nearby_almost_duplicate(Solution, nums, index_diff, value_diff)
    result
    return (result,)


@app.cell
def _(assert_contains_nearby_almost_duplicate, expected, result):
    assert_contains_nearby_almost_duplicate(result, expected)
    return


if __name__ == "__main__":
    app.run()
