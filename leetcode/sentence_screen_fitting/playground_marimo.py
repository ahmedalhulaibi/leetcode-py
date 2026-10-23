import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_words_typing, run_words_typing
    from solution import Solution

    return Solution, assert_words_typing, run_words_typing


@app.cell
def _():
    # Example test case
    sentence = ["hello", "world"]
    rows = 2
    cols = 8
    expected = 1
    return cols, expected, rows, sentence


@app.cell
def _(Solution, cols, rows, run_words_typing, sentence):
    result = run_words_typing(Solution, sentence, rows, cols)
    result
    return (result,)


@app.cell
def _(assert_words_typing, expected, result):
    assert_words_typing(result, expected)
    return


if __name__ == "__main__":
    app.run()
