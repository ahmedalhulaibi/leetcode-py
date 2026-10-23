import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_length_of_last_word, run_length_of_last_word
    from solution import Solution

    return Solution, assert_length_of_last_word, run_length_of_last_word


@app.cell
def _():
    # Example test case
    s = "Hello World"
    expected = 5
    return expected, s


@app.cell
def _(Solution, run_length_of_last_word, s):
    result = run_length_of_last_word(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_length_of_last_word, expected, result):
    assert_length_of_last_word(result, expected)
    return


if __name__ == "__main__":
    app.run()
