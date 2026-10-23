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
    arr = [1, 3, 5]
    expected = 4
    return arr, expected


@app.cell
def _(Solution, arr, run_num_of_subarrays):
    result = run_num_of_subarrays(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_num_of_subarrays, expected, result):
    assert_num_of_subarrays(result, expected)
    return


if __name__ == "__main__":
    app.run()
