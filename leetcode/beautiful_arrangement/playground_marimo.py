import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_arrangement, run_count_arrangement
    from solution import Solution

    return Solution, assert_count_arrangement, run_count_arrangement


@app.cell
def _():
    # Example test case
    n = 2
    expected = 2
    return expected, n


@app.cell
def _(Solution, n, run_count_arrangement):
    result = run_count_arrangement(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_count_arrangement, expected, result):
    assert_count_arrangement(result, expected)
    return


if __name__ == "__main__":
    app.run()
