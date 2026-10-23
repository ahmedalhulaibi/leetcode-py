import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_words_abbreviation, run_words_abbreviation
    from solution import Solution

    return Solution, assert_words_abbreviation, run_words_abbreviation


@app.cell
def _():
    # Example test case
    words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
    expected = ["l2e", "god", "internal", "me", "i6t", "interval", "inte4n", "f2e", "intr4n"]
    return expected, words


@app.cell
def _(Solution, run_words_abbreviation, words):
    result = run_words_abbreviation(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_words_abbreviation, expected, result):
    assert_words_abbreviation(result, expected)
    return


if __name__ == "__main__":
    app.run()
