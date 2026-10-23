import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_happy_string, run_get_happy_string
    from solution import Solution

    return Solution, assert_get_happy_string, run_get_happy_string


@app.cell
def _():
    # Example test case
    n = 3
    k = 9
    expected = "cab"
    return expected, k, n


@app.cell
def _(Solution, k, n, run_get_happy_string):
    result = run_get_happy_string(Solution, n, k)
    result
    return (result,)


@app.cell
def _(assert_get_happy_string, expected, result):
    assert_get_happy_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
