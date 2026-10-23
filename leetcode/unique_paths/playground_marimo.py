import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_unique_paths, run_unique_paths
    from solution import Solution

    return Solution, assert_unique_paths, run_unique_paths


@app.cell
def _():
    # Example test case
    m = 3
    n = 7
    expected = 28
    return expected, m, n


@app.cell
def _(Solution, m, n, run_unique_paths):
    result = run_unique_paths(Solution, m, n)
    result
    return (result,)


@app.cell
def _(assert_unique_paths, expected, result):
    assert_unique_paths(result, expected)
    return


if __name__ == "__main__":
    app.run()
