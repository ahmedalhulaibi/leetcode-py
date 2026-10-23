import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_generate_matrix, run_generate_matrix
    from solution import Solution

    return Solution, assert_generate_matrix, run_generate_matrix


@app.cell
def _():
    # Example test case
    n = 3
    expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    return expected, n


@app.cell
def _(Solution, n, run_generate_matrix):
    result = run_generate_matrix(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_generate_matrix, expected, result):
    assert_generate_matrix(result, expected)
    return


if __name__ == "__main__":
    app.run()
