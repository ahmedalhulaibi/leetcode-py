import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_max_or_subsets, run_count_max_or_subsets
    from solution import Solution

    return Solution, assert_count_max_or_subsets, run_count_max_or_subsets


@app.cell
def _():
    # Example test case
    nums = [3, 1]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums, run_count_max_or_subsets):
    result = run_count_max_or_subsets(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_count_max_or_subsets, expected, result):
    assert_count_max_or_subsets(result, expected)
    return


if __name__ == "__main__":
    app.run()
