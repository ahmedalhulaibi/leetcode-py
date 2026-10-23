import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_unguarded, run_count_unguarded
    from solution import Solution

    return Solution, assert_count_unguarded, run_count_unguarded


@app.cell
def _():
    # Example test case
    m = 4
    n = 6
    guards = [[0, 0], [1, 1], [2, 3]]
    walls = [[0, 1], [2, 2], [1, 4]]
    expected = 7
    return expected, guards, m, n, walls


@app.cell
def _(Solution, guards, m, n, run_count_unguarded, walls):
    result = run_count_unguarded(Solution, m, n, guards, walls)
    result
    return (result,)


@app.cell
def _(assert_count_unguarded, expected, result):
    assert_count_unguarded(result, expected)
    return


if __name__ == "__main__":
    app.run()
