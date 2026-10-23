import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_row, run_get_row
    from solution import Solution

    return Solution, assert_get_row, run_get_row


@app.cell
def _():
    # Example test case
    row_index: int = 3
    expected: list[int] = [1, 3, 3, 1]
    return expected, row_index


@app.cell
def _(Solution, row_index: int, run_get_row):
    result = run_get_row(Solution, row_index)
    result
    return (result,)


@app.cell
def _(assert_get_row, expected: list[int], result):
    assert_get_row(result, expected)
    return


if __name__ == "__main__":
    app.run()
