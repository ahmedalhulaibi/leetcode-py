import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_integers, run_find_integers
    from solution import Solution

    return Solution, assert_find_integers, run_find_integers


@app.cell
def _():
    # Example test case
    n = 5
    expected = 5
    return expected, n


@app.cell
def _(Solution, n, run_find_integers):
    result = run_find_integers(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_find_integers, expected, result):
    assert_find_integers(result, expected)
    return


if __name__ == "__main__":
    app.run()
