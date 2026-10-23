import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_palindrome, run_largest_palindrome
    from solution import Solution

    return Solution, assert_largest_palindrome, run_largest_palindrome


@app.cell
def _():
    # Example test case
    n = 2
    expected = 987
    return expected, n


@app.cell
def _(Solution, n, run_largest_palindrome):
    result = run_largest_palindrome(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_largest_palindrome, expected, result):
    assert_largest_palindrome(result, expected)
    return


if __name__ == "__main__":
    app.run()
