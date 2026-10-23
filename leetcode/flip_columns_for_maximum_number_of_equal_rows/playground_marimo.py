import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_equal_rows_after_flips, run_max_equal_rows_after_flips
    from solution import Solution

    return (
        Solution,
        assert_max_equal_rows_after_flips,
        run_max_equal_rows_after_flips,
    )


@app.cell
def _():
    # Example test case
    matrix = [[0, 1], [1, 0]]
    expected = 2
    return expected, matrix


@app.cell
def _(Solution, matrix, run_max_equal_rows_after_flips):
    result = run_max_equal_rows_after_flips(Solution, matrix)
    result
    return (result,)


@app.cell
def _(assert_max_equal_rows_after_flips, expected, result):
    assert_max_equal_rows_after_flips(result, expected)
    return


if __name__ == "__main__":
    app.run()
