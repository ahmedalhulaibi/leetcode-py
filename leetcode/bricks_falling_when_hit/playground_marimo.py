import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_hit_bricks, run_hit_bricks
    from solution import Solution

    return Solution, assert_hit_bricks, run_hit_bricks


@app.cell
def _():
    # Example test case
    grid = [[1, 0, 0, 0], [1, 1, 1, 0]]
    hits = [[1, 0]]
    expected = [2]
    return expected, grid, hits


@app.cell
def _(Solution, grid, hits, run_hit_bricks):
    result = run_hit_bricks(Solution, grid, hits)
    result
    return (result,)


@app.cell
def _(assert_hit_bricks, expected, result):
    assert_hit_bricks(result, expected)
    return


if __name__ == "__main__":
    app.run()
