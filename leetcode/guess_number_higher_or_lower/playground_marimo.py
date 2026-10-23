import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_guess_number, run_guess_number
    from solution import Solution

    return Solution, assert_guess_number, run_guess_number


@app.cell
def _():
    # Example test case
    n = 10
    pick = 6
    expected = 6
    return expected, n, pick


@app.cell
def _(Solution, n, pick, run_guess_number):
    result = run_guess_number(Solution, n, pick)
    result
    return (result,)


@app.cell
def _(assert_guess_number, expected, result):
    assert_guess_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
