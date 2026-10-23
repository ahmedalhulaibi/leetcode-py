import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_magnificent_sets, run_magnificent_sets
    from solution import Solution

    return Solution, assert_magnificent_sets, run_magnificent_sets


@app.cell
def _():
    # Example test case
    n = 6
    edges = [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]
    expected = 4
    return edges, expected, n


@app.cell
def _(Solution, edges, n, run_magnificent_sets):
    result = run_magnificent_sets(Solution, n, edges)
    result
    return (result,)


@app.cell
def _(assert_magnificent_sets, expected, result):
    assert_magnificent_sets(result, expected)
    return


if __name__ == "__main__":
    app.run()
