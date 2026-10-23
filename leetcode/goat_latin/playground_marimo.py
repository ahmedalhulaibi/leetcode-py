import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_to_goat_latin, run_to_goat_latin
    from solution import Solution

    return Solution, assert_to_goat_latin, run_to_goat_latin


@app.cell
def _():
    # Example test case
    sentence = "I speak Goat Latin"
    expected = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    return expected, sentence


@app.cell
def _(Solution, run_to_goat_latin, sentence):
    result = run_to_goat_latin(Solution, sentence)
    result
    return (result,)


@app.cell
def _(assert_to_goat_latin, expected, result):
    assert_to_goat_latin(result, expected)
    return


if __name__ == "__main__":
    app.run()
