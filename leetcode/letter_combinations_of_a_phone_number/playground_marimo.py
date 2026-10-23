import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_letter_combinations, run_letter_combinations
    from solution import Solution

    return Solution, assert_letter_combinations, run_letter_combinations


@app.cell
def _():
    # Example test case
    digits = "23"
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    return digits, expected


@app.cell
def _(Solution, digits, run_letter_combinations):
    result = run_letter_combinations(Solution, digits)
    result
    return (result,)


@app.cell
def _(assert_letter_combinations, expected, result):
    assert_letter_combinations(result, expected)
    return


if __name__ == "__main__":
    app.run()
