import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_words, run_find_words
    from solution import Solution

    return Solution, assert_find_words, run_find_words


@app.cell
def _():
    # Example test case
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    expected = ["eat", "oath"]
    return board, expected, words


@app.cell
def _(Solution, board, run_find_words, words):
    result = run_find_words(Solution, board, words)
    result
    return (result,)


@app.cell
def _(assert_find_words, expected, result):
    assert_find_words(result, expected)
    return


if __name__ == "__main__":
    app.run()
