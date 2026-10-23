import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_valid_palindrome, run_valid_palindrome
    from solution import Solution

    return Solution, assert_valid_palindrome, run_valid_palindrome


@app.cell
def _():
    # Example test case
    s = "abca"
    expected = True
    return expected, s


@app.cell
def _(Solution, run_valid_palindrome, s):
    result = run_valid_palindrome(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_valid_palindrome, expected, result):
    assert_valid_palindrome(result, expected)
    return


if __name__ == "__main__":
    app.run()
