import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_nth_super_ugly_number, run_nth_super_ugly_number
    from solution import Solution

    return Solution, assert_nth_super_ugly_number, run_nth_super_ugly_number


@app.cell
def _():
    # Example test case
    n = 12
    primes = [2, 7, 13, 19]
    expected = 32
    return expected, n, primes


@app.cell
def _(Solution, n, primes, run_nth_super_ugly_number):
    result = run_nth_super_ugly_number(Solution, n, primes)
    result
    return (result,)


@app.cell
def _(assert_nth_super_ugly_number, expected, result):
    assert_nth_super_ugly_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
