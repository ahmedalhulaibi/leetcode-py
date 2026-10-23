import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_palindrome, run_is_palindrome
    from solution import Solution

    return Solution, assert_is_palindrome, run_is_palindrome


@app.cell
def _():
    # Example test case
    x = 121
    expected = True
    return expected, x


@app.cell
def _(Solution, run_is_palindrome, x):
    result = run_is_palindrome(Solution, x)
    result
    return (result,)


@app.cell
def _(assert_is_palindrome, expected, result):
    assert_is_palindrome(result, expected)
    return


if __name__ == "__main__":
    app.run()
