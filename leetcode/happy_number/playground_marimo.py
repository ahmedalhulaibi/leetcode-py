import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_happy, run_is_happy
    from solution import Solution

    return Solution, assert_is_happy, run_is_happy


@app.cell
def _():
    # Example test case
    n = 19
    expected = True
    return expected, n


@app.cell
def _(Solution, n, run_is_happy):
    result = run_is_happy(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_is_happy, expected, result):
    assert_is_happy(result, expected)
    return


if __name__ == "__main__":
    app.run()
