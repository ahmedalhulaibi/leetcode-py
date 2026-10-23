import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_closest_primes, run_closest_primes
    from solution import Solution

    return Solution, assert_closest_primes, run_closest_primes


@app.cell
def _():
    # Example test case
    left: int = 10
    right: int = 19
    expected: list[int] = [11, 13]
    return expected, left, right


@app.cell
def _(Solution, left: int, right: int, run_closest_primes):
    result = run_closest_primes(Solution, left, right)
    result
    return (result,)


@app.cell
def _(assert_closest_primes, expected: list[int], result):
    assert_closest_primes(result, expected)
    return


if __name__ == "__main__":
    app.run()
