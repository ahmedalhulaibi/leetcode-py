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
    s = "011101"
    expected = 5
    return expected, s


@app.cell
def _(Solution, run_max_score, s):
    result = run_max_score(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_max_score, expected, result):
    assert_max_score(result, expected)
    return


if __name__ == "__main__":
    app.run()
