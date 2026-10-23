import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_valid_word_square, run_valid_word_square
    from solution import Solution

    return Solution, assert_valid_word_square, run_valid_word_square


@app.cell
def _():
    # Example test case
    words = ["abcd", "bnrt", "crmy", "dtye"]
    expected = True
    return expected, words


@app.cell
def _(Solution, run_valid_word_square, words):
    result = run_valid_word_square(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_valid_word_square, expected, result):
    assert_valid_word_square(result, expected)
    return


if __name__ == "__main__":
    app.run()
