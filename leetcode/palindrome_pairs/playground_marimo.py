import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_palindrome_pairs, run_palindrome_pairs
    from solution import Solution

    return Solution, assert_palindrome_pairs, run_palindrome_pairs


@app.cell
def _():
    # Example test case
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    expected = [[0, 1], [1, 0], [3, 2], [2, 4]]
    return expected, words


@app.cell
def _(Solution, run_palindrome_pairs, words):
    result = run_palindrome_pairs(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_palindrome_pairs, expected, result):
    assert_palindrome_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
