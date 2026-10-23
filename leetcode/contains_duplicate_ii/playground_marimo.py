import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_contains_nearby_duplicate, run_contains_nearby_duplicate
    from solution import Solution

    return (
        Solution,
        assert_contains_nearby_duplicate,
        run_contains_nearby_duplicate,
    )


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 1]
    k = 3
    expected = True
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_contains_nearby_duplicate):
    result = run_contains_nearby_duplicate(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_contains_nearby_duplicate, expected, result):
    assert_contains_nearby_duplicate(result, expected)
    return


if __name__ == "__main__":
    app.run()
