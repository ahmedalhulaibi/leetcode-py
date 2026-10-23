import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_judge_square_sum, run_judge_square_sum
    from solution import Solution

    return Solution, assert_judge_square_sum, run_judge_square_sum


@app.cell
def _():
    # Example test case
    c = 5
    expected = True
    return c, expected


@app.cell
def _(Solution, c, run_judge_square_sum):
    result = run_judge_square_sum(Solution, c)
    result
    return (result,)


@app.cell
def _(assert_judge_square_sum, expected, result):
    assert_judge_square_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
