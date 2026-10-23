import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_multiply, run_multiply
    from solution import Solution

    return Solution, assert_multiply, run_multiply


@app.cell
def _():
    # Example test case
    mat1 = [[1, 0, 0], [-1, 0, 3]]
    mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    expected = [[7, 0, 0], [-7, 0, 3]]
    return expected, mat1, mat2


@app.cell
def _(Solution, mat1, mat2, run_multiply):
    result = run_multiply(Solution, mat1, mat2)
    result
    return (result,)


@app.cell
def _(assert_multiply, expected, result):
    assert_multiply(result, expected)
    return


if __name__ == "__main__":
    app.run()
