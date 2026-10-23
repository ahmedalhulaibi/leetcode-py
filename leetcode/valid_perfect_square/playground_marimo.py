import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_perfect_square, run_is_perfect_square
    from solution import Solution

    return Solution, assert_is_perfect_square, run_is_perfect_square


@app.cell
def _():
    # Example test case
    num = 16
    expected = True
    return expected, num


@app.cell
def _(Solution, num, run_is_perfect_square):
    result = run_is_perfect_square(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_is_perfect_square, expected, result):
    assert_is_perfect_square(result, expected)
    return


if __name__ == "__main__":
    app.run()
