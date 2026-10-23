import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_line, run_longest_line
    from solution import Solution

    return Solution, assert_longest_line, run_longest_line


@app.cell
def _():
    # Example test case
    mat = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
    expected = 3
    return expected, mat


@app.cell
def _(Solution, mat, run_longest_line):
    result = run_longest_line(Solution, mat)
    result
    return (result,)


@app.cell
def _(assert_longest_line, expected, result):
    assert_longest_line(result, expected)
    return


if __name__ == "__main__":
    app.run()
