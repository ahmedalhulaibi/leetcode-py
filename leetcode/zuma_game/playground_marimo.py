import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_min_step, run_find_min_step
    from solution import Solution

    return Solution, assert_find_min_step, run_find_min_step


@app.cell
def _():
    # Example test case
    board = "WWRRBBWW"
    hand = "WRBRW"
    expected = 2
    return board, expected, hand


@app.cell
def _(Solution, board, hand, run_find_min_step):
    result = run_find_min_step(Solution, board, hand)
    result
    return (result,)


@app.cell
def _(assert_find_min_step, expected, result):
    assert_find_min_step(result, expected)
    return


if __name__ == "__main__":
    app.run()
