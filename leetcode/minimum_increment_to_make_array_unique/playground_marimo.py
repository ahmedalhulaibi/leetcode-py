import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_increment_for_unique, run_min_increment_for_unique
    from solution import Solution

    return (
        Solution,
        assert_min_increment_for_unique,
        run_min_increment_for_unique,
    )


@app.cell
def _():
    # Example test case
    nums = [3, 2, 1, 2, 1, 7]
    expected = 6
    return expected, nums


@app.cell
def _(Solution, nums, run_min_increment_for_unique):
    result = run_min_increment_for_unique(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_min_increment_for_unique, expected, result):
    assert_min_increment_for_unique(result, expected)
    return


if __name__ == "__main__":
    app.run()
