import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_win_nim, run_can_win_nim
    from solution import Solution

    return Solution, assert_can_win_nim, run_can_win_nim


@app.cell
def _():
    # Example test case
    n = 4
    expected = False
    return expected, n


@app.cell
def _(Solution, n, run_can_win_nim):
    result = run_can_win_nim(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_can_win_nim, expected, result):
    assert_can_win_nim(result, expected)
    return


if __name__ == "__main__":
    app.run()
