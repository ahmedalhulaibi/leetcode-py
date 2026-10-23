import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_word_pattern, run_word_pattern
    from solution import Solution

    return Solution, assert_word_pattern, run_word_pattern


@app.cell
def _():
    # Example test case
    pattern = "abba"
    s = "dog cat cat dog"
    expected = True
    return expected, pattern, s


@app.cell
def _(Solution, pattern, run_word_pattern, s):
    result = run_word_pattern(Solution, pattern, s)
    result
    return (result,)


@app.cell
def _(assert_word_pattern, expected, result):
    assert_word_pattern(result, expected)
    return


if __name__ == "__main__":
    app.run()
