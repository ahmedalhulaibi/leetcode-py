import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_append_characters, run_append_characters
    from solution import Solution

    return Solution, assert_append_characters, run_append_characters


@app.cell
def _():
    # Example test case
    s = "coaching"
    t = "coding"
    expected = 4
    return expected, s, t


@app.cell
def _(Solution, run_append_characters, s, t):
    result = run_append_characters(Solution, s, t)
    result
    return (result,)


@app.cell
def _(assert_append_characters, expected, result):
    assert_append_characters(result, expected)
    return


if __name__ == "__main__":
    app.run()
