import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_primes, run_count_primes
    from solution import Solution

    return Solution, assert_count_primes, run_count_primes


@app.cell
def _():
    # Example test case
    n: int = 10
    expected: int = 4
    return expected, n


@app.cell
def _(Solution, n: int, run_count_primes):
    result = run_count_primes(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_count_primes, expected: int, result):
    assert_count_primes(result, expected)
    return


if __name__ == "__main__":
    app.run()
