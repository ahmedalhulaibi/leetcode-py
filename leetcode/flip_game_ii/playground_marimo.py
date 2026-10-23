import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_win, run_can_win
    from solution import Solution

    return Solution, assert_can_win, run_can_win


@app.cell
def _():
    # Example test case
    current_state = "++++"
    expected = True
    return current_state, expected


@app.cell
def _(Solution, current_state, run_can_win):
    result = run_can_win(Solution, current_state)
    result
    return (result,)


@app.cell
def _(assert_can_win, expected, result):
    assert_can_win(result, expected)
    return


if __name__ == "__main__":
    app.run()
