import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_construct_2d_array, run_construct_2d_array
    from solution import Solution

    return Solution, assert_construct_2d_array, run_construct_2d_array


@app.cell
def _():
    # Example test case
    original = [1, 2, 3, 4]
    m = 2
    n = 2
    expected = [[1, 2], [3, 4]]
    return expected, m, n, original


@app.cell
def _(Solution, m, n, original, run_construct_2d_array):
    result = run_construct_2d_array(Solution, original, m, n)
    result
    return (result,)


@app.cell
def _(assert_construct_2d_array, expected, result):
    assert_construct_2d_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
