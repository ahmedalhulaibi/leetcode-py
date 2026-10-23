import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rotate_the_box, run_rotate_the_box
    from solution import Solution

    return Solution, assert_rotate_the_box, run_rotate_the_box


@app.cell
def _():
    # Example test case
    box_grid = [["#", ".", "#"]]
    expected = [["."], ["#"], ["#"]]
    return box_grid, expected


@app.cell
def _(Solution, box_grid, run_rotate_the_box):
    result = run_rotate_the_box(Solution, box_grid)
    result
    return (result,)


@app.cell
def _(assert_rotate_the_box, expected, result):
    assert_rotate_the_box(result, expected)
    return


if __name__ == "__main__":
    app.run()
