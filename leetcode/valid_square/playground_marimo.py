import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_valid_square, run_valid_square
    from solution import Solution

    return Solution, assert_valid_square, run_valid_square


@app.cell
def _():
    # Example test case
    p1 = [0, 0]
    p2 = [1, 1]
    p3 = [1, 0]
    p4 = [0, 1]
    expected = True
    return expected, p1, p2, p3, p4


@app.cell
def _(Solution, p1, p2, p3, p4, run_valid_square):
    result = run_valid_square(Solution, p1, p2, p3, p4)
    result
    return (result,)


@app.cell
def _(assert_valid_square, expected, result):
    assert_valid_square(result, expected)
    return


if __name__ == "__main__":
    app.run()
