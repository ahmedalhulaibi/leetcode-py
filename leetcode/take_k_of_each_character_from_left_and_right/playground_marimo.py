import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_take_characters, run_take_characters
    from solution import Solution

    return Solution, assert_take_characters, run_take_characters


@app.cell
def _():
    # Example test case
    s = "aabaaaacaabc"
    k = 2
    expected = 8
    return expected, k, s


@app.cell
def _(Solution, k, run_take_characters, s):
    result = run_take_characters(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_take_characters, expected, result):
    assert_take_characters(result, expected)
    return


if __name__ == "__main__":
    app.run()
