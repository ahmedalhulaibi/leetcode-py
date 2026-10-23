import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_enclaves, run_num_enclaves
    from solution import Solution

    return Solution, assert_num_enclaves, run_num_enclaves


@app.cell
def _():
    # Example test case
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    expected = 3
    return expected, grid


@app.cell
def _(Solution, grid, run_num_enclaves):
    result = run_num_enclaves(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_num_enclaves, expected, result):
    assert_num_enclaves(result, expected)
    return


if __name__ == "__main__":
    app.run()
