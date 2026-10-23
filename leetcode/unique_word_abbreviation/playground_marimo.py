import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_valid_word_abbr, run_valid_word_abbr
    from solution import ValidWordAbbr

    return ValidWordAbbr, assert_valid_word_abbr, run_valid_word_abbr


@app.cell
def _():
    # Example test case
    operations = ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"]
    inputs = [["deer", "door", "cake", "card"], ["dear"], ["cart"], ["cane"]]
    expected = [None, False, True, False]
    return expected, inputs, operations


@app.cell
def _(ValidWordAbbr, inputs, operations, run_valid_word_abbr):
    result, implementation = run_valid_word_abbr(ValidWordAbbr, operations, inputs)
    print(result)
    implementation
    return (result,)


@app.cell
def _(assert_valid_word_abbr, expected, result):
    assert_valid_word_abbr(result, expected)
    return


if __name__ == "__main__":
    app.run()
