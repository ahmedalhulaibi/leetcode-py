import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_convert, run_convert
    from solution import Solution

    return Solution, assert_convert, run_convert


@app.cell
def _():
    # Example test case
    s = "PAYPALISHIRING"
    num_rows = 3
    expected = "PAHNAPLSIIGYIR"
    return expected, num_rows, s


@app.cell
def _(Solution, num_rows, run_convert, s):
    result = run_convert(Solution, s, num_rows)
    result
    return (result,)


@app.cell
def _(assert_convert, expected, result):
    assert_convert(result, expected)
    return


if __name__ == "__main__":
    app.run()
