import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_tile_possibilities, run_num_tile_possibilities
    from solution import Solution

    return Solution, assert_num_tile_possibilities, run_num_tile_possibilities


@app.cell
def _():
    # Example test case
    tiles = "AAB"
    expected = 8
    return expected, tiles


@app.cell
def _(Solution, run_num_tile_possibilities, tiles):
    result = run_num_tile_possibilities(Solution, tiles)
    result
    return (result,)


@app.cell
def _(assert_num_tile_possibilities, expected, result):
    assert_num_tile_possibilities(result, expected)
    return


if __name__ == "__main__":
    app.run()
