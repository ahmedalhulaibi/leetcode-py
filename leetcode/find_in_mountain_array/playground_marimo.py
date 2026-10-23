import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_in_mountain_array, run_find_in_mountain_array
    from solution import Solution

    return Solution, assert_find_in_mountain_array, run_find_in_mountain_array


@app.cell
def _():
    # Example test case
    arr = [1, 2, 3, 4, 5, 3, 1]
    target = 3
    expected = 2
    return arr, expected, target


@app.cell
def _(Solution, arr, run_find_in_mountain_array, target):
    result = run_find_in_mountain_array(Solution, arr, target)
    result
    return (result,)


@app.cell
def _(assert_find_in_mountain_array, expected, result):
    assert_find_in_mountain_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
