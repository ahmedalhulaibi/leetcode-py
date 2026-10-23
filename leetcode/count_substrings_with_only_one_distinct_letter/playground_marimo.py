import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_letters, run_count_letters
    from solution import Solution

    return Solution, assert_count_letters, run_count_letters


@app.cell
def _():
    # Example test case
    s = "aaaba"
    expected = 8
    return expected, s


@app.cell
def _(Solution, run_count_letters, s):
    result = run_count_letters(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_count_letters, expected, result):
    assert_count_letters(result, expected)
    return


if __name__ == "__main__":
    app.run()
