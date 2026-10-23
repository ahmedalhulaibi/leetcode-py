import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shifting_letters, run_shifting_letters
    from solution import Solution

    return Solution, assert_shifting_letters, run_shifting_letters


@app.cell
def _():
    # Example test case
    s = "abc"
    shifts = [3, 5, 9]
    expected = "rpl"
    return expected, s, shifts


@app.cell
def _(Solution, run_shifting_letters, s, shifts):
    result = run_shifting_letters(Solution, s, shifts)
    result
    return (result,)


@app.cell
def _(assert_shifting_letters, expected, result):
    assert_shifting_letters(result, expected)
    return


if __name__ == "__main__":
    app.run()
