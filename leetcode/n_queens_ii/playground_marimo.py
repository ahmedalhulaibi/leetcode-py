import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_total_n_queens, run_total_n_queens
    from solution import Solution

    return Solution, assert_total_n_queens, run_total_n_queens


@app.cell
def _():
    # Example test case
    n = 4
    expected = 2
    return expected, n


@app.cell
def _(Solution, n, run_total_n_queens):
    result = run_total_n_queens(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_total_n_queens, expected, result):
    assert_total_n_queens(result, expected)
    return


if __name__ == "__main__":
    app.run()
