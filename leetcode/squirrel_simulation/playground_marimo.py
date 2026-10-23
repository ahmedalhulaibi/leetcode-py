import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_distance, run_min_distance
    from solution import Solution

    return Solution, assert_min_distance, run_min_distance


@app.cell
def _():
    # Example test case
    height = 5
    width = 7
    tree = [2, 2]
    squirrel = [4, 4]
    nuts = [[3, 0], [2, 5]]
    expected = 12
    return expected, height, nuts, squirrel, tree, width


@app.cell
def _(Solution, height, nuts, run_min_distance, squirrel, tree, width):
    result = run_min_distance(Solution, height, width, tree, squirrel, nuts)
    result
    return (result,)


@app.cell
def _(assert_min_distance, expected, result):
    assert_min_distance(result, expected)
    return


if __name__ == "__main__":
    app.run()
