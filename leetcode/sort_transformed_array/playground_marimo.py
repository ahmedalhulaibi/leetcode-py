import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sort_transformed_array, run_sort_transformed_array
    from solution import Solution

    return Solution, assert_sort_transformed_array, run_sort_transformed_array


@app.cell
def _():
    # Example test case
    nums: list[int] = [-4, -2, 2, 4]
    a = 1
    b = 3
    c = 5
    expected = [3, 9, 15, 33]
    return a, b, c, expected, nums


@app.cell
def _(Solution, a, b, c, nums: list[int], run_sort_transformed_array):
    result = run_sort_transformed_array(Solution, nums, a, b, c)
    result
    return (result,)


@app.cell
def _(assert_sort_transformed_array, expected, result):
    assert_sort_transformed_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
