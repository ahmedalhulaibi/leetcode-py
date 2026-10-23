import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_word, run_longest_word
    from solution import Solution

    return Solution, assert_longest_word, run_longest_word


@app.cell
def _():
    # Example test case
    words = ["w", "wo", "wor", "worl", "world"]
    expected = "world"
    return expected, words


@app.cell
def _(Solution, run_longest_word, words):
    result = run_longest_word(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_longest_word, expected, result):
    assert_longest_word(result, expected)
    return


if __name__ == "__main__":
    app.run()
