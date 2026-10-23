import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_construct, run_construct
    from solution import Solution

    return Solution, assert_construct, run_construct


@app.cell
def _():
    # Example test case (each node serialized as [isLeaf, val])
    grid = [[0, 1], [1, 0]]
    expected = [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]
    return expected, grid


@app.cell
def _(Solution, grid, run_construct):
    result = run_construct(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_construct, expected, result):
    assert_construct(result, expected)
    return


if __name__ == "__main__":
    app.run()
