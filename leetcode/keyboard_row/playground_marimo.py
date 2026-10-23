import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_words, run_find_words
    from solution import Solution

    return Solution, assert_find_words, run_find_words


@app.cell
def _():
    # Example test case
    words: list[str] = ["Hello", "Alaska", "Dad", "Peace"]
    expected: list[str] = ["Alaska", "Dad"]
    return expected, words


@app.cell
def _(Solution, run_find_words, words: list[str]):
    result = run_find_words(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_find_words, expected: list[str], result):
    assert_find_words(result, expected)
    return


if __name__ == "__main__":
    app.run()
