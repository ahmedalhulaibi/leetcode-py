import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_character_replacement, run_character_replacement
    from solution import Solution

    return Solution, assert_character_replacement, run_character_replacement


@app.cell
def _():
    # Example test case
    s = "ABAB"
    k = 2
    expected = 4
    return expected, k, s


@app.cell
def _(Solution, k, run_character_replacement, s):
    result = run_character_replacement(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_character_replacement, expected, result):
    assert_character_replacement(result, expected)
    return


if __name__ == "__main__":
    app.run()
