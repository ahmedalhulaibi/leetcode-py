import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_common_chars, run_common_chars
    from solution import Solution

    return Solution, assert_common_chars, run_common_chars


@app.cell
def _():
    # Example test case
    words = ["bella", "label", "roller"]
    expected = ["e", "l", "l"]
    return expected, words


@app.cell
def _(Solution, run_common_chars, words):
    result = run_common_chars(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_common_chars, expected, result):
    assert_common_chars(result, expected)
    return


if __name__ == "__main__":
    app.run()
