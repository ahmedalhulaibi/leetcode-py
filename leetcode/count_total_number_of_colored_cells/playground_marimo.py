import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_colored_cells, run_colored_cells
    from solution import Solution

    return Solution, assert_colored_cells, run_colored_cells


@app.cell
def _():
    # Example test case
    n = 3
    expected = 13
    return expected, n


@app.cell
def _(Solution, n, run_colored_cells):
    result = run_colored_cells(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_colored_cells, expected, result):
    assert_colored_cells(result, expected)
    return


if __name__ == "__main__":
    app.run()
