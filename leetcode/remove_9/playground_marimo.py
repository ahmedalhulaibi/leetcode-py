import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_new_integer, run_new_integer
    from solution import Solution

    return Solution, assert_new_integer, run_new_integer


@app.cell
def _():
    # Example test case
    n = 9
    expected = 10
    return expected, n


@app.cell
def _(Solution, n, run_new_integer):
    result = run_new_integer(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_new_integer, expected, result):
    assert_new_integer(result, expected)
    return


if __name__ == "__main__":
    app.run()
