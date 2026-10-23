import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_of_subarrays, run_num_of_subarrays
    from solution import Solution

    return Solution, assert_num_of_subarrays, run_num_of_subarrays


@app.cell
def _():
    # Example test case
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    expected = 3
    return arr, expected, k, threshold


@app.cell
def _(Solution, arr, k, run_num_of_subarrays, threshold):
    result = run_num_of_subarrays(Solution, arr, k, threshold)
    result
    return (result,)


@app.cell
def _(assert_num_of_subarrays, expected, result):
    assert_num_of_subarrays(result, expected)
    return


if __name__ == "__main__":
    app.run()
