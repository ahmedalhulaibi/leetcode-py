import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_subarrays_div_by_k, run_subarrays_div_by_k
    from solution import Solution

    return Solution, assert_subarrays_div_by_k, run_subarrays_div_by_k


@app.cell
def _():
    # Example test case
    nums = [4, 5, 0, -2, -3, 1]
    k = 5
    expected = 7
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_subarrays_div_by_k):
    result = run_subarrays_div_by_k(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_subarrays_div_by_k, expected, result):
    assert_subarrays_div_by_k(result, expected)
    return


if __name__ == "__main__":
    app.run()
