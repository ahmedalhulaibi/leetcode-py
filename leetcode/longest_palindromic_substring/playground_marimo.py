import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_palindrome, run_longest_palindrome
    from solution import Solution

    return Solution, assert_longest_palindrome, run_longest_palindrome


@app.cell
def _():
    # Example test case
    s = "babad"
    expected = {"bab", "aba"}
    return expected, s


@app.cell
def _(Solution, run_longest_palindrome, s):
    result = run_longest_palindrome(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_longest_palindrome, expected, result):
    assert_longest_palindrome(result, expected)
    return


if __name__ == "__main__":
    app.run()
