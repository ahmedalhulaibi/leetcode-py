import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_all_possible_fbt, run_all_possible_fbt
    from solution import Solution

    return Solution, assert_all_possible_fbt, run_all_possible_fbt


@app.cell
def _():
    # Example test case
    n = 5
    expected = [[0, 0, 0, None, None, 0, 0], [0, 0, 0, 0, 0]]
    return expected, n


@app.cell
def _(Solution, n, run_all_possible_fbt):
    result = run_all_possible_fbt(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_all_possible_fbt, expected, result):
    assert_all_possible_fbt(result, expected)
    return


if __name__ == "__main__":
    app.run()
