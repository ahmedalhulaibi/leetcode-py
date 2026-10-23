import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_increasing_path, run_longest_increasing_path
    from solution import Solution

    return (
        Solution,
        assert_longest_increasing_path,
        run_longest_increasing_path,
    )


@app.cell
def _():
    # Example test case
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    expected = 4
    return expected, matrix


@app.cell
def _(Solution, matrix, run_longest_increasing_path):
    result = run_longest_increasing_path(Solution, matrix)
    result
    return (result,)


@app.cell
def _(assert_longest_increasing_path, expected, result):
    assert_longest_increasing_path(result, expected)
    return


if __name__ == "__main__":
    app.run()
