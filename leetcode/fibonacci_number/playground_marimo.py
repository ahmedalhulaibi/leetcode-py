import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_fib, run_fib
    from solution import Solution

    return Solution, assert_fib, run_fib


@app.cell
def _():
    # Example test case
    n = 2
    expected = 1
    return expected, n


@app.cell
def _(Solution, n, run_fib):
    result = run_fib(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_fib, expected, result):
    assert_fib(result, expected)
    return


if __name__ == "__main__":
    app.run()
