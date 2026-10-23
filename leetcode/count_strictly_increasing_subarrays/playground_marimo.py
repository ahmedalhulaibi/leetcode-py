import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_strictly_increasing, run_count_strictly_increasing
    from solution import Solution

    return (
        Solution,
        assert_count_strictly_increasing,
        run_count_strictly_increasing,
    )


@app.cell
def _():
    # Example test case
    nums = [1, 3, 5, 4, 4, 6]
    expected = 10
    return expected, nums


@app.cell
def _(Solution, nums, run_count_strictly_increasing):
    result = run_count_strictly_increasing(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_count_strictly_increasing, expected, result):
    assert_count_strictly_increasing(result, expected)
    return


if __name__ == "__main__":
    app.run()
