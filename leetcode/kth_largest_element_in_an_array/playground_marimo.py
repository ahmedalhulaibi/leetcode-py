import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_kth_largest, run_find_kth_largest
    from solution import Solution

    return Solution, assert_find_kth_largest, run_find_kth_largest


@app.cell
def _():
    # Example test case
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    expected = 5
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_find_kth_largest):
    result = run_find_kth_largest(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_find_kth_largest, expected, result):
    assert_find_kth_largest(result, expected)
    return


if __name__ == "__main__":
    app.run()
