import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_characters, run_count_characters
    from solution import Solution

    return Solution, assert_count_characters, run_count_characters


@app.cell
def _():
    # Example test case
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    expected = 6
    return chars, expected, words


@app.cell
def _(Solution, chars, run_count_characters, words):
    result = run_count_characters(Solution, words, chars)
    result
    return (result,)


@app.cell
def _(assert_count_characters, expected, result):
    assert_count_characters(result, expected)
    return


if __name__ == "__main__":
    app.run()
