import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_results_array, run_results_array
    from solution import Solution

    return Solution, assert_results_array, run_results_array


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 4, 3, 2, 5]
    k = 3
    expected = [3, 4, -1, -1, -1]
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_results_array):
    result = run_results_array(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_results_array, expected, result):
    assert_results_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
