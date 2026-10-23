import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_champagne_tower, run_champagne_tower
    from solution import Solution

    return Solution, assert_champagne_tower, run_champagne_tower


@app.cell
def _():
    # Example test case
    poured = 1
    query_row = 1
    query_glass = 1
    expected = 0.0
    return expected, poured, query_glass, query_row


@app.cell
def _(Solution, poured, query_glass, query_row, run_champagne_tower):
    result = run_champagne_tower(Solution, poured, query_row, query_glass)
    result
    return (result,)


@app.cell
def _(assert_champagne_tower, expected, result):
    assert_champagne_tower(result, expected)
    return


if __name__ == "__main__":
    app.run()
