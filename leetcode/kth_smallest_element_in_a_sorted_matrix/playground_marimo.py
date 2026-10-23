import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_kth_smallest, run_kth_smallest
    from solution import Solution

    return Solution, assert_kth_smallest, run_kth_smallest


@app.cell
def _():
    # Example test case
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    expected = 13
    return expected, k, matrix


@app.cell
def _(Solution, k, matrix, run_kth_smallest):
    result = run_kth_smallest(Solution, matrix, k)
    result
    return (result,)


@app.cell
def _(assert_kth_smallest, expected, result):
    assert_kth_smallest(result, expected)
    return


if __name__ == "__main__":
    app.run()
