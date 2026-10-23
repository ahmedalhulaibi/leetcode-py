import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_valid_palindrome, run_is_valid_palindrome
    from solution import Solution

    return Solution, assert_is_valid_palindrome, run_is_valid_palindrome


@app.cell
def _():
    # Example test case
    s = "abcdeca"
    k = 2
    expected = True
    return expected, k, s


@app.cell
def _(Solution, k, run_is_valid_palindrome, s):
    result = run_is_valid_palindrome(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_is_valid_palindrome, expected, result):
    assert_is_valid_palindrome(result, expected)
    return


if __name__ == "__main__":
    app.run()
