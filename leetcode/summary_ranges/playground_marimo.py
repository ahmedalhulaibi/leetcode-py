import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_summary_ranges, run_summary_ranges
    from solution import Solution

    return Solution, assert_summary_ranges, run_summary_ranges


@app.cell
def _():
    # Example test case
    nums = [0, 1, 2, 4, 5, 7]
    expected = ["0->2", "4->5", "7"]
    return expected, nums


@app.cell
def _(Solution, nums, run_summary_ranges):
    result = run_summary_ranges(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_summary_ranges, expected, result):
    assert_summary_ranges(result, expected)
    return


if __name__ == "__main__":
    app.run()
