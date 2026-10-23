import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_mountain_removals, run_minimum_mountain_removals
    from solution import Solution

    return (
        Solution,
        assert_minimum_mountain_removals,
        run_minimum_mountain_removals,
    )


@app.cell
def _():
    # Example test case
    nums = [2, 1, 1, 5, 6, 2, 3, 1]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums, run_minimum_mountain_removals):
    result = run_minimum_mountain_removals(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_minimum_mountain_removals, expected, result):
    assert_minimum_mountain_removals(result, expected)
    return


if __name__ == "__main__":
    app.run()
