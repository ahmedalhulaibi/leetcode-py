import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_submatrix_sum_target, run_num_submatrix_sum_target
    from solution import Solution

    return (
        Solution,
        assert_num_submatrix_sum_target,
        run_num_submatrix_sum_target,
    )


@app.cell
def _():
    # Example test case
    matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    target = 0
    expected = 4
    return expected, matrix, target


@app.cell
def _(Solution, matrix, run_num_submatrix_sum_target, target):
    result = run_num_submatrix_sum_target(Solution, matrix, target)
    result
    return (result,)


@app.cell
def _(assert_num_submatrix_sum_target, expected, result):
    assert_num_submatrix_sum_target(result, expected)
    return


if __name__ == "__main__":
    app.run()
