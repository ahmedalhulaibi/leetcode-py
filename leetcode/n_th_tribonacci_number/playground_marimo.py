import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_tribonacci, run_tribonacci
    from solution import Solution

    return Solution, assert_tribonacci, run_tribonacci


@app.cell
def _():
    # Example test case
    n = 4
    expected = 4
    return expected, n


@app.cell
def _(Solution, n, run_tribonacci):
    result = run_tribonacci(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_tribonacci, expected, result):
    assert_tribonacci(result, expected)
    return


if __name__ == "__main__":
    app.run()
