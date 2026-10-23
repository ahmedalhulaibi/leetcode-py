import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_beautiful_array, run_beautiful_array
    from solution import Solution

    return Solution, assert_beautiful_array, run_beautiful_array


@app.cell
def _():
    # Example test case
    n = 4
    expected = 4
    return expected, n


@app.cell
def _(Solution, n, run_beautiful_array):
    result = run_beautiful_array(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_beautiful_array, expected, result):
    assert_beautiful_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
