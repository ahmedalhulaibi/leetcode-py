import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_score_of_string, run_score_of_string
    from solution import Solution

    return Solution, assert_score_of_string, run_score_of_string


@app.cell
def _():
    # Example test case
    s = "hello"
    expected = 13
    return expected, s


@app.cell
def _(Solution, run_score_of_string, s):
    result = run_score_of_string(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_score_of_string, expected, result):
    assert_score_of_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
