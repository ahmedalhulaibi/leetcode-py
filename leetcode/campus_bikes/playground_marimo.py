import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_assign_bikes, run_assign_bikes
    from solution import Solution

    return Solution, assert_assign_bikes, run_assign_bikes


@app.cell
def _():
    # Example test case
    workers = [[0, 0], [2, 1]]
    bikes = [[1, 2], [3, 3]]
    expected = [1, 0]
    return bikes, expected, workers


@app.cell
def _(Solution, bikes, run_assign_bikes, workers):
    result = run_assign_bikes(Solution, workers, bikes)
    result
    return (result,)


@app.cell
def _(assert_assign_bikes, expected, result):
    assert_assign_bikes(result, expected)
    return


if __name__ == "__main__":
    app.run()
