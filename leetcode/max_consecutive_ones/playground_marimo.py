import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_max_consecutive_ones, run_find_max_consecutive_ones
    from solution import Solution

    return (
        Solution,
        assert_find_max_consecutive_ones,
        run_find_max_consecutive_ones,
    )


@app.cell
def _():
    # Example test case
    nums = [1, 1, 0, 1, 1, 1]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums, run_find_max_consecutive_ones):
    result = run_find_max_consecutive_ones(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_max_consecutive_ones, expected, result):
    assert_find_max_consecutive_ones(result, expected)
    return


if __name__ == "__main__":
    app.run()
