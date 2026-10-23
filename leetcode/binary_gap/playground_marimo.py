import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_binary_gap, run_binary_gap
    from solution import Solution

    return Solution, assert_binary_gap, run_binary_gap


@app.cell
def _():
    # Example test case
    n = 22
    expected = 2
    return expected, n


@app.cell
def _(Solution, n, run_binary_gap):
    result = run_binary_gap(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_binary_gap, expected, result):
    assert_binary_gap(result, expected)
    return


if __name__ == "__main__":
    app.run()
