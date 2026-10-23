import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_search_matrix, run_search_matrix
    from solution import Solution

    return Solution, assert_search_matrix, run_search_matrix


@app.cell
def _():
    # Example test case
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    expected = True
    return expected, matrix, target


@app.cell
def _(Solution, matrix, run_search_matrix, target):
    result = run_search_matrix(Solution, matrix, target)
    result
    return (result,)


@app.cell
def _(assert_search_matrix, expected, result):
    assert_search_matrix(result, expected)
    return


if __name__ == "__main__":
    app.run()
