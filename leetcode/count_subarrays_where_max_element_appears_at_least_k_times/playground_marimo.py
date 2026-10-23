import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_subarrays, run_count_subarrays
    from solution import Solution

    return Solution, assert_count_subarrays, run_count_subarrays


@app.cell
def _():
    # Example test case
    nums = [1, 3, 2, 3, 3]
    k = 2
    expected = 6
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_count_subarrays):
    result = run_count_subarrays(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_count_subarrays, expected, result):
    assert_count_subarrays(result, expected)
    return


if __name__ == "__main__":
    app.run()
