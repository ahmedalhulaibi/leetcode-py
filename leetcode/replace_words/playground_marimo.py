import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_replace_words, run_replace_words
    from solution import Solution

    return Solution, assert_replace_words, run_replace_words


@app.cell
def _():
    # Example test case
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    expected = "the cat was rat by the bat"
    return dictionary, expected, sentence


@app.cell
def _(Solution, dictionary, run_replace_words, sentence):
    result = run_replace_words(Solution, dictionary, sentence)
    result
    return (result,)


@app.cell
def _(assert_replace_words, expected, result):
    assert_replace_words(result, expected)
    return


if __name__ == "__main__":
    app.run()
