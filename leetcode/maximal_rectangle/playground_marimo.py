import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximal_rectangle, run_maximal_rectangle
    from solution import Solution

    return Solution, assert_maximal_rectangle, run_maximal_rectangle


@app.cell
def _():
    # Example test case
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    expected = 6
    return expected, matrix


@app.cell
def _(Solution, matrix, run_maximal_rectangle):
    result = run_maximal_rectangle(Solution, matrix)
    result
    return (result,)


@app.cell
def _(assert_maximal_rectangle, expected, result):
    assert_maximal_rectangle(result, expected)
    return


if __name__ == "__main__":
    app.run()
