import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_valid_mountain_array, run_valid_mountain_array
    from solution import Solution

    return Solution, assert_valid_mountain_array, run_valid_mountain_array


@app.cell
def _():
    # Example test case
    arr = [0, 3, 2, 1]
    expected = True
    return arr, expected


@app.cell
def _(Solution, arr, run_valid_mountain_array):
    result = run_valid_mountain_array(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_valid_mountain_array, expected, result):
    assert_valid_mountain_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
