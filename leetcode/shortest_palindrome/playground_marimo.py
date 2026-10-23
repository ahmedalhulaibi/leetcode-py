import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shortest_palindrome, run_shortest_palindrome
    from solution import Solution

    return Solution, assert_shortest_palindrome, run_shortest_palindrome


@app.cell
def _():
    # Example test case
    s = "aacecaaa"
    expected = "aaacecaaa"
    return expected, s


@app.cell
def _(Solution, run_shortest_palindrome, s):
    result = run_shortest_palindrome(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_shortest_palindrome, expected, result):
    assert_shortest_palindrome(result, expected)
    return


if __name__ == "__main__":
    app.run()
