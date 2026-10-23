import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_transform_array, run_transform_array
    from solution import Solution

    return Solution, assert_transform_array, run_transform_array


@app.cell
def _():
    # Example test case
    arr = [6, 2, 3, 4]
    expected = [6, 3, 3, 4]
    return arr, expected


@app.cell
def _(Solution, arr, run_transform_array):
    result = run_transform_array(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_transform_array, expected, result):
    assert_transform_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
