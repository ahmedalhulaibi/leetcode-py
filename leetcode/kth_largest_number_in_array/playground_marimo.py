import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_kth_largest_number, run_kth_largest_number
    from solution import Solution

    return Solution, assert_kth_largest_number, run_kth_largest_number


@app.cell
def _():
    # Example test case
    nums = ["3", "6", "7", "10"]
    k = 4
    expected = "3"
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_kth_largest_number):
    result = run_kth_largest_number(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_kth_largest_number, expected, result):
    assert_kth_largest_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
