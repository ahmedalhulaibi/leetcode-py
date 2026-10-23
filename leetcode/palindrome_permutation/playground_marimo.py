import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_permute_palindrome, run_can_permute_palindrome
    from solution import Solution

    return Solution, assert_can_permute_palindrome, run_can_permute_palindrome


@app.cell
def _():
    # Example test case
    s = "carerac"
    expected = True
    return expected, s


@app.cell
def _(Solution, run_can_permute_palindrome, s):
    result = run_can_permute_palindrome(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_can_permute_palindrome, expected, result):
    assert_can_permute_palindrome(result, expected)
    return


if __name__ == "__main__":
    app.run()
