import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_safeness_factor, run_maximum_safeness_factor
    from solution import Solution

    return (
        Solution,
        assert_maximum_safeness_factor,
        run_maximum_safeness_factor,
    )


@app.cell
def _():
    # Example test case
    grid: list[list[int]] = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
    expected = 2
    return expected, grid


@app.cell
def _(Solution, grid: list[list[int]], run_maximum_safeness_factor):
    result = run_maximum_safeness_factor(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_maximum_safeness_factor, expected, result):
    assert_maximum_safeness_factor(result, expected)
    return


if __name__ == "__main__":
    app.run()
