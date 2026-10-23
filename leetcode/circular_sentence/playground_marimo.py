import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_circular_sentence, run_is_circular_sentence
    from solution import Solution

    return Solution, assert_is_circular_sentence, run_is_circular_sentence


@app.cell
def _():
    # Example test case
    sentence = "leetcode exercises sound delightful"
    expected = True
    return expected, sentence


@app.cell
def _(Solution, run_is_circular_sentence, sentence):
    result = run_is_circular_sentence(Solution, sentence)
    result
    return (result,)


@app.cell
def _(assert_is_circular_sentence, expected, result):
    assert_is_circular_sentence(result, expected)
    return


if __name__ == "__main__":
    app.run()
