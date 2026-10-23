import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimized_maximum, run_minimized_maximum
    from solution import Solution

    return Solution, assert_minimized_maximum, run_minimized_maximum


@app.cell
def _():
    # Example test case
    n = 6
    quantities = [11, 6]
    expected = 3
    return expected, n, quantities


@app.cell
def _(Solution, n, quantities, run_minimized_maximum):
    result = run_minimized_maximum(Solution, n, quantities)
    result
    return (result,)


@app.cell
def _(assert_minimized_maximum, expected, result):
    assert_minimized_maximum(result, expected)
    return


if __name__ == "__main__":
    app.run()
