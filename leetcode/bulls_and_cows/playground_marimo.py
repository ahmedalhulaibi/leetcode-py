import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_hint, run_get_hint
    from solution import Solution

    return Solution, assert_get_hint, run_get_hint


@app.cell
def _():
    # Example test case
    secret = "1807"
    guess = "7810"
    expected = "1A3B"
    return expected, guess, secret


@app.cell
def _(Solution, guess, run_get_hint, secret):
    result = run_get_hint(Solution, secret, guess)
    result
    return (result,)


@app.cell
def _(assert_get_hint, expected, result):
    assert_get_hint(result, expected)
    return


if __name__ == "__main__":
    app.run()
