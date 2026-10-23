import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_islands2, run_num_islands2
    from solution import Solution

    return Solution, assert_num_islands2, run_num_islands2


@app.cell
def _():
    # Example test case
    m = 3
    n = 3
    positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
    expected = [1, 1, 2, 3]
    return expected, m, n, positions


@app.cell
def _(Solution, m, n, positions, run_num_islands2):
    result = run_num_islands2(Solution, m, n, positions)
    result
    return (result,)


@app.cell
def _(assert_num_islands2, expected, result):
    assert_num_islands2(result, expected)
    return


if __name__ == "__main__":
    app.run()
