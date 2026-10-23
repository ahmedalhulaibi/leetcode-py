import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_judge, run_find_judge
    from solution import Solution

    return Solution, assert_find_judge, run_find_judge


@app.cell
def _():
    # Example test case
    n = 3
    trust = [[1, 3], [2, 3]]
    expected = 3
    return expected, n, trust


@app.cell
def _(Solution, n, run_find_judge, trust):
    result = run_find_judge(Solution, n, trust)
    result
    return (result,)


@app.cell
def _(assert_find_judge, expected, result):
    assert_find_judge(result, expected)
    return


if __name__ == "__main__":
    app.run()
