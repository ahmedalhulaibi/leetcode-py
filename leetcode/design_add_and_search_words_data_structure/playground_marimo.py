import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_word_dictionary, run_word_dictionary
    from solution import WordDictionary

    return WordDictionary, assert_word_dictionary, run_word_dictionary


@app.cell
def _():
    # Example test case
    operations = [
        "WordDictionary",
        "addWord",
        "addWord",
        "addWord",
        "search",
        "search",
        "search",
        "search",
    ]
    inputs = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
    expected = [None, None, None, None, False, True, True, True]
    return expected, inputs, operations


@app.cell
def _(WordDictionary, inputs, operations, run_word_dictionary):
    result = run_word_dictionary(WordDictionary, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_word_dictionary, expected, result):
    assert_word_dictionary(result, expected)
    return


if __name__ == "__main__":
    app.run()
