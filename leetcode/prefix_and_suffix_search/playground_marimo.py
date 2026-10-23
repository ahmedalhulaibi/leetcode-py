import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_word_filter, run_word_filter
    from solution import WordFilter

    return WordFilter, assert_word_filter, run_word_filter


@app.cell
def _():
    # Example test case
    operations = ["WordFilter", "f"]
    inputs = [["apple"], ["a", "e"]]
    expected = [None, 0]
    return expected, inputs, operations


@app.cell
def _(WordFilter, inputs, operations, run_word_filter):
    result, word_filter = run_word_filter(WordFilter, operations, inputs)
    print(result)
    word_filter
    return (result,)


@app.cell
def _(assert_word_filter, expected, result):
    assert_word_filter(result, expected)
    return


if __name__ == "__main__":
    app.run()
