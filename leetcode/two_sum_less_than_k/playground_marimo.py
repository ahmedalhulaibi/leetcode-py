import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_two_sum_less_than_k, run_two_sum_less_than_k
    from solution import Solution

    return Solution, assert_two_sum_less_than_k, run_two_sum_less_than_k


@app.cell
def _():
    # Example test case
    nums = [34, 23, 1, 24, 75, 33, 54, 8]
    k = 60
    expected = 58
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_two_sum_less_than_k):
    result = run_two_sum_less_than_k(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_two_sum_less_than_k, expected, result):
    assert_two_sum_less_than_k(result, expected)
    return


if __name__ == "__main__":
    app.run()
