import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_score, run_maximum_score
    from solution import Solution

    return Solution, assert_maximum_score, run_maximum_score


@app.cell
def _():
    # Example test case
    nums = [8, 3, 9, 3, 8]
    k = 2
    expected = 81
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_maximum_score):
    result = run_maximum_score(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_maximum_score, expected, result):
    assert_maximum_score(result, expected)
    return


if __name__ == "__main__":
    app.run()
