import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_median_sliding_window, run_median_sliding_window
    from solution import Solution

    return Solution, assert_median_sliding_window, run_median_sliding_window


@app.cell
def _():
    # Example test case
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_median_sliding_window):
    result = run_median_sliding_window(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_median_sliding_window, expected, result):
    assert_median_sliding_window(result, expected)
    return


if __name__ == "__main__":
    app.run()
