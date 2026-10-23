import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_judge_circle, run_judge_circle
    from solution import Solution

    return Solution, assert_judge_circle, run_judge_circle


@app.cell
def _():
    # Example test case
    moves = "UD"
    expected = True
    return expected, moves


@app.cell
def _(Solution, moves, run_judge_circle):
    result = run_judge_circle(Solution, moves)
    result
    return (result,)


@app.cell
def _(assert_judge_circle, expected, result):
    assert_judge_circle(result, expected)
    return


if __name__ == "__main__":
    app.run()
