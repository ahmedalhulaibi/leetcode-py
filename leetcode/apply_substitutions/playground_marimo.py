import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_apply_substitutions, run_apply_substitutions
    from solution import Solution

    return Solution, assert_apply_substitutions, run_apply_substitutions


@app.cell
def _():
    # Example test case
    replacements = [["A", "abc"], ["B", "def"]]
    text = "%A%_%B%"
    expected = "abc_def"
    return expected, replacements, text


@app.cell
def _(Solution, replacements, run_apply_substitutions, text):
    result = run_apply_substitutions(Solution, replacements, text)
    result
    return (result,)


@app.cell
def _(assert_apply_substitutions, expected, result):
    assert_apply_substitutions(result, expected)
    return


if __name__ == "__main__":
    app.run()
