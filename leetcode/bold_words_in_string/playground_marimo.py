import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_bold_words, run_bold_words
    from solution import Solution

    return Solution, assert_bold_words, run_bold_words


@app.cell
def _():
    # Example test case
    words = ["ab", "bc"]
    s = "aabcd"
    expected = "a<b>abc</b>d"
    return expected, s, words


@app.cell
def _(Solution, run_bold_words, s, words):
    result = run_bold_words(Solution, words, s)
    result
    return (result,)


@app.cell
def _(assert_bold_words, expected, result):
    assert_bold_words(result, expected)
    return


if __name__ == "__main__":
    app.run()
