import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_components, run_count_components
    from solution import Solution

    return Solution, assert_count_components, run_count_components


@app.cell
def _():
    # Example test case
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    expected = 2
    return edges, expected, n


@app.cell
def _(Solution, edges, n, run_count_components):
    result = run_count_components(Solution, n, edges)
    result
    return (result,)


@app.cell
def _(assert_count_components, expected, result):
    assert_count_components(result, expected)
    return


if __name__ == "__main__":
    app.run()
