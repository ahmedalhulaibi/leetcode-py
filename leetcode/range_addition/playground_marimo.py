import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_modified_array, run_get_modified_array
    from solution import Solution

    return Solution, assert_get_modified_array, run_get_modified_array


@app.cell
def _():
    # Example test case
    length = 5
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    expected = [-2, 0, 3, 5, 3]
    return expected, length, updates


@app.cell
def _(Solution, length, run_get_modified_array, updates):
    result = run_get_modified_array(Solution, length, updates)
    result
    return (result,)


@app.cell
def _(assert_get_modified_array, expected, result):
    assert_get_modified_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
