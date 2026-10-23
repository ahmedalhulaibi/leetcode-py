import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_knight_dialer, run_knight_dialer
    from solution import Solution

    return Solution, assert_knight_dialer, run_knight_dialer


@app.cell
def _():
    # Example test case
    n = 2
    expected = 20
    return expected, n


@app.cell
def _(Solution, n, run_knight_dialer):
    result = run_knight_dialer(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_knight_dialer, expected, result):
    assert_knight_dialer(result, expected)
    return


if __name__ == "__main__":
    app.run()
