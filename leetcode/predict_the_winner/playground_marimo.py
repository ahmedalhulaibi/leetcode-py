import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_predict_the_winner, run_predict_the_winner
    from solution import Solution

    return Solution, assert_predict_the_winner, run_predict_the_winner


@app.cell
def _():
    # Example test case
    nums = [1, 5, 233, 7]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_predict_the_winner):
    result = run_predict_the_winner(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_predict_the_winner, expected, result):
    assert_predict_the_winner(result, expected)
    return


if __name__ == "__main__":
    app.run()
