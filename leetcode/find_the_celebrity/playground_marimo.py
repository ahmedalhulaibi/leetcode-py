import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_celebrity, run_find_celebrity
    from solution import Solution

    return Solution, assert_find_celebrity, run_find_celebrity


@app.cell
def _():
    # Example test case
    graph = [[1, 1, 0], [0, 1, 0], [1, 1, 1]]
    expected = 1
    return expected, graph


@app.cell
def _(Solution, graph, run_find_celebrity):
    result = run_find_celebrity(Solution, graph)
    result
    return (result,)


@app.cell
def _(assert_find_celebrity, expected, result):
    assert_find_celebrity(result, expected)
    return


if __name__ == "__main__":
    app.run()
