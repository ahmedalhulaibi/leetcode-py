import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_gray_code, run_gray_code
    from solution import Solution

    return Solution, assert_gray_code, run_gray_code


@app.cell
def _():
    # Example test case
    n = 2
    expected_size = 4
    return expected_size, n


@app.cell
def _(Solution, n, run_gray_code):
    result = run_gray_code(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_gray_code, expected_size, result):
    assert_gray_code(result, expected_size)
    return


if __name__ == "__main__":
    app.run()
