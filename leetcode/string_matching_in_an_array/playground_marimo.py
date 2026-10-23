import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_string_matching, run_string_matching
    from solution import Solution

    return Solution, assert_string_matching, run_string_matching


@app.cell
def _():
    # Example test case
    words = ["mass", "as", "hero", "superhero"]
    expected = ["as", "hero"]
    return expected, words


@app.cell
def _(Solution, run_string_matching, words):
    result = run_string_matching(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_string_matching, expected, result):
    assert_string_matching(result, expected)
    return


if __name__ == "__main__":
    app.run()
