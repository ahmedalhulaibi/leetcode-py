import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_relative_sort_array, run_relative_sort_array
    from solution import Solution

    return Solution, assert_relative_sort_array, run_relative_sort_array


@app.cell
def _():
    # Example test case
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    expected = [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    return arr1, arr2, expected


@app.cell
def _(Solution, arr1, arr2, run_relative_sort_array):
    result = run_relative_sort_array(Solution, arr1, arr2)
    result
    return (result,)


@app.cell
def _(assert_relative_sort_array, expected, result):
    assert_relative_sort_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
