import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_word_pattern_match, run_word_pattern_match
    from solution import Solution

    return Solution, assert_word_pattern_match, run_word_pattern_match


@app.cell
def _():
    # Example test case
    pattern = "abab"
    s = "redblueredblue"
    expected = True
    return expected, pattern, s


@app.cell
def _(Solution, pattern, run_word_pattern_match, s):
    result = run_word_pattern_match(Solution, pattern, s)
    result
    return (result,)


@app.cell
def _(assert_word_pattern_match, expected, result):
    assert_word_pattern_match(result, expected)
    return


if __name__ == "__main__":
    app.run()
