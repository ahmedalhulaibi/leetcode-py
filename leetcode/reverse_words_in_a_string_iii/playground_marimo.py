import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reverse_words, run_reverse_words
    from solution import Solution

    return Solution, assert_reverse_words, run_reverse_words


@app.cell
def _():
    # Example test case
    s = "Mr Ding"
    expected = "rM gniD"
    return expected, s


@app.cell
def _(Solution, run_reverse_words, s):
    result = run_reverse_words(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_reverse_words, expected, result):
    assert_reverse_words(result, expected)
    return


if __name__ == "__main__":
    app.run()
