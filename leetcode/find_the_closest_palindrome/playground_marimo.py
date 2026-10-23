import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_nearest_palindromic, run_nearest_palindromic
    from solution import Solution

    return Solution, assert_nearest_palindromic, run_nearest_palindromic


@app.cell
def _():
    # Example test case
    n = "123"
    expected = "121"
    return expected, n


@app.cell
def _(Solution, n, run_nearest_palindromic):
    result = run_nearest_palindromic(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_nearest_palindromic, expected, result):
    assert_nearest_palindromic(result, expected)
    return


if __name__ == "__main__":
    app.run()
