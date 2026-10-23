import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_valid_word_abbreviation, run_valid_word_abbreviation
    from solution import Solution

    return (
        Solution,
        assert_valid_word_abbreviation,
        run_valid_word_abbreviation,
    )


@app.cell
def _():
    # Example test case
    word = "internationalization"
    abbr = "i12iz4n"
    expected = True
    return abbr, expected, word


@app.cell
def _(Solution, abbr, run_valid_word_abbreviation, word):
    result = run_valid_word_abbreviation(Solution, word, abbr)
    result
    return (result,)


@app.cell
def _(assert_valid_word_abbreviation, expected, result):
    assert_valid_word_abbreviation(result, expected)
    return


if __name__ == "__main__":
    app.run()
