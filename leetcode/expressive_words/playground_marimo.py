import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_expressive_words, run_expressive_words
    from solution import Solution

    return Solution, assert_expressive_words, run_expressive_words


@app.cell
def _():
    # Example test case
    s = "heeellooo"
    words = ["hello", "hi", "helo"]
    expected = 1
    return expected, s, words


@app.cell
def _(Solution, run_expressive_words, s, words):
    result = run_expressive_words(Solution, s, words)
    result
    return (result,)


@app.cell
def _(assert_expressive_words, expected, result):
    assert_expressive_words(result, expected)
    return


if __name__ == "__main__":
    app.run()
