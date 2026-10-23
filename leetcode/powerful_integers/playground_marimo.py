import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_powerful_integers, run_powerful_integers
    from solution import Solution

    return Solution, assert_powerful_integers, run_powerful_integers


@app.cell
def _():
    # Example test case
    x = 2
    y = 3
    bound = 10
    expected = [2, 3, 4, 5, 7, 9, 10]
    return bound, expected, x, y


@app.cell
def _(Solution, bound, run_powerful_integers, x, y):
    result = run_powerful_integers(Solution, x, y, bound)
    result
    return (result,)


@app.cell
def _(assert_powerful_integers, expected, result):
    assert_powerful_integers(result, expected)
    return


if __name__ == "__main__":
    app.run()
