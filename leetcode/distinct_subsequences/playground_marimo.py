import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_distinct, run_num_distinct
    from solution import Solution

    return Solution, assert_num_distinct, run_num_distinct


@app.cell
def _():
    # Example test case
    s = "rabbbit"
    t = "rabbit"
    expected = 3
    return expected, s, t


@app.cell
def _(Solution, run_num_distinct, s, t):
    result = run_num_distinct(Solution, s, t)
    result
    return (result,)


@app.cell
def _(assert_num_distinct, expected, result):
    assert_num_distinct(result, expected)
    return


if __name__ == "__main__":
    app.run()
