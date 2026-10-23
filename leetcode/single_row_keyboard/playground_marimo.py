import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_calculate_time, run_calculate_time
    from solution import Solution

    return Solution, assert_calculate_time, run_calculate_time


@app.cell
def _():
    # Example test case
    keyboard = "abcdefghijklmnopqrstuvwxyz"
    word = "cba"
    expected = 4
    return expected, keyboard, word


@app.cell
def _(Solution, keyboard, run_calculate_time, word):
    result = run_calculate_time(Solution, keyboard, word)
    result
    return (result,)


@app.cell
def _(assert_calculate_time, expected, result):
    assert_calculate_time(result, expected)
    return


if __name__ == "__main__":
    app.run()
