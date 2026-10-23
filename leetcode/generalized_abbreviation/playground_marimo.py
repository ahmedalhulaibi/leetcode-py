import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_generate_abbreviations, run_generate_abbreviations
    from solution import Solution

    return Solution, assert_generate_abbreviations, run_generate_abbreviations


@app.cell
def _():
    # Example test case
    word = "word"
    expected = [
        "4",
        "3d",
        "2r1",
        "2rd",
        "1o2",
        "1o1d",
        "1or1",
        "1ord",
        "w3",
        "w2d",
        "w1r1",
        "w1rd",
        "wo2",
        "wo1d",
        "wor1",
        "word",
    ]
    return expected, word


@app.cell
def _(Solution, run_generate_abbreviations, word):
    result = run_generate_abbreviations(Solution, word)
    result
    return (result,)


@app.cell
def _(assert_generate_abbreviations, expected, result):
    assert_generate_abbreviations(result, expected)
    return


if __name__ == "__main__":
    app.run()
