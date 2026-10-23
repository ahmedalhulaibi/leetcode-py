import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_word_squares, run_word_squares
    from solution import Solution

    return Solution, assert_word_squares, run_word_squares


@app.cell
def _():
    # Example test case
    words = ["area", "lead", "wall", "lady", "ball"]
    expected = [["ball", "area", "lead", "lady"], ["wall", "area", "lead", "lady"]]
    return expected, words


@app.cell
def _(Solution, run_word_squares, words):
    result = run_word_squares(Solution, words)
    result
    return (result,)


@app.cell
def _(assert_word_squares, expected, result):
    assert_word_squares(result, expected)
    return


if __name__ == "__main__":
    app.run()
