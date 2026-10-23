import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reverse_only_letters, run_reverse_only_letters
    from solution import Solution

    return Solution, assert_reverse_only_letters, run_reverse_only_letters


@app.cell
def _():
    # Example test case
    s = "ab-cd"
    expected = "dc-ba"
    return expected, s


@app.cell
def _(Solution, run_reverse_only_letters, s):
    result = run_reverse_only_letters(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_reverse_only_letters, expected, result):
    assert_reverse_only_letters(result, expected)
    return


if __name__ == "__main__":
    app.run()
