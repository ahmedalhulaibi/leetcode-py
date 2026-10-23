import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_number_of_subarrays, run_number_of_subarrays
    from solution import Solution

    return Solution, assert_number_of_subarrays, run_number_of_subarrays


@app.cell
def _():
    # Example test case
    nums = [1, 1, 2, 1, 1]
    k = 3
    expected = 2
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_number_of_subarrays):
    result = run_number_of_subarrays(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_number_of_subarrays, expected, result):
    assert_number_of_subarrays(result, expected)
    return


if __name__ == "__main__":
    app.run()
