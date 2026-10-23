import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_prime_palindrome, run_prime_palindrome
    from solution import Solution

    return Solution, assert_prime_palindrome, run_prime_palindrome


@app.cell
def _():
    # Example test case
    n: int = 6
    expected: int = 7
    return expected, n


@app.cell
def _(Solution, n: int, run_prime_palindrome):
    result = run_prime_palindrome(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_prime_palindrome, expected: int, result):
    assert_prime_palindrome(result, expected)
    return


if __name__ == "__main__":
    app.run()
