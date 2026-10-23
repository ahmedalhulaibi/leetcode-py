import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_servers, run_count_servers
    from solution import Solution

    return Solution, assert_count_servers, run_count_servers


@app.cell
def _():
    # Example test case
    grid = [[1, 0], [1, 1]]
    expected = 3
    return expected, grid


@app.cell
def _(Solution, grid, run_count_servers):
    result = run_count_servers(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_count_servers, expected, result):
    assert_count_servers(result, expected)
    return


if __name__ == "__main__":
    app.run()
