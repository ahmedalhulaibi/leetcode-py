import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_add_bold_tag, run_add_bold_tag
    from solution import Solution

    return Solution, assert_add_bold_tag, run_add_bold_tag


@app.cell
def _():
    # Example test case
    s = "abcxyz123"
    words = ["abc", "123"]
    expected = "<b>abc</b>xyz<b>123</b>"
    return expected, s, words


@app.cell
def _(Solution, run_add_bold_tag, s, words):
    result = run_add_bold_tag(Solution, s, words)
    result
    return (result,)


@app.cell
def _(assert_add_bold_tag, expected, result):
    assert_add_bold_tag(result, expected)
    return


if __name__ == "__main__":
    app.run()
