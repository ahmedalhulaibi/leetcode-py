import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_first_palindrome, run_first_palindrome
    from solution import Solution

    return Solution, assert_first_palindrome, run_first_palindrome


@app.cell
def _():
    # Example test case
    words = ["abc", "car", "ada", "racecar", "cool"]
    expected = "ada"
    return expected, words


@app.cell
def _(Solution, run_first_palindrome, words):
    result = run_first_palindrome(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_first_palindrome, expected, result):
    assert_first_palindrome(result, expected)
    return


if __name__ == "__main__":
    app.run()
