import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_effort_path, run_minimum_effort_path
    from solution import Solution

    return Solution, assert_minimum_effort_path, run_minimum_effort_path


@app.cell
def _():
    # Example test case
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    expected = 2
    return expected, heights


@app.cell
def _(Solution, heights, run_minimum_effort_path):
    result = run_minimum_effort_path(Solution, heights)
    result
    return (result,)


@app.cell
def _(assert_minimum_effort_path, expected, result):
    assert_minimum_effort_path(result, expected)
    return


if __name__ == "__main__":
    app.run()
