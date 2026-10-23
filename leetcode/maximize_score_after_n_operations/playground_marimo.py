import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_score, run_max_score
    from solution import Solution

    return Solution, assert_max_score, run_max_score


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 4, 5, 6]
    expected = 14
    return expected, nums


@app.cell
def _(Solution, nums, run_max_score):
    result = run_max_score(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_max_score, expected, result):
    assert_max_score(result, expected)
    return


if __name__ == "__main__":
    app.run()
