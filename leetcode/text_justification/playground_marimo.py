import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_full_justify, run_full_justify
    from solution import Solution

    return Solution, assert_full_justify, run_full_justify


@app.cell
def _():
    # Example test case
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    max_width = 16
    expected = ["This    is    an", "example  of text", "justification.  "]
    return expected, max_width, words


@app.cell
def _(Solution, max_width, run_full_justify, words):
    result = run_full_justify(Solution, words, max_width)
    result
    return (result,)


@app.cell
def _(assert_full_justify, expected, result):
    assert_full_justify(result, expected)
    return


if __name__ == "__main__":
    app.run()
