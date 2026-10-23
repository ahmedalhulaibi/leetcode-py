import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_valid_utf8, run_valid_utf8
    from solution import Solution

    return Solution, assert_valid_utf8, run_valid_utf8


@app.cell
def _():
    # Example test case
    data = [197, 130, 1]
    expected = True
    return data, expected


@app.cell
def _(Solution, data, run_valid_utf8):
    result = run_valid_utf8(Solution, data)
    result
    return (result,)


@app.cell
def _(assert_valid_utf8, expected, result):
    assert_valid_utf8(result, expected)
    return


if __name__ == "__main__":
    app.run()
