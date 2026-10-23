import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_a, run_max_a
    from solution import Solution

    return Solution, assert_max_a, run_max_a


@app.cell
def _():
    # Example test case
    n = 7
    expected = 9
    return expected, n


@app.cell
def _(Solution, n, run_max_a):
    result = run_max_a(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_max_a, expected, result):
    assert_max_a(result, expected)
    return


if __name__ == "__main__":
    app.run()
