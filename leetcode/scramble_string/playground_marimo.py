import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_scramble, run_is_scramble
    from solution import Solution

    return Solution, assert_is_scramble, run_is_scramble


@app.cell
def _():
    # Example test case
    s1 = "great"
    s2 = "rgeat"
    expected = True
    return expected, s1, s2


@app.cell
def _(Solution, run_is_scramble, s1, s2):
    result = run_is_scramble(Solution, s1, s2)
    result
    return (result,)


@app.cell
def _(assert_is_scramble, expected, result):
    assert_is_scramble(result, expected)
    return


if __name__ == "__main__":
    app.run()
