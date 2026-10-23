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
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22]]
    target = 5
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
