import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_i_win, run_can_i_win
    from solution import Solution

    return Solution, assert_can_i_win, run_can_i_win


@app.cell
def _():
    # Example test case
    max_choosable_integer = 10
    desired_total = 11
    expected = False
    return desired_total, expected, max_choosable_integer


@app.cell
def _(Solution, desired_total, max_choosable_integer, run_can_i_win):
    result = run_can_i_win(Solution, max_choosable_integer, desired_total)
    result
    return (result,)


@app.cell
def _(assert_can_i_win, expected, result):
    assert_can_i_win(result, expected)
    return


if __name__ == "__main__":
    app.run()
