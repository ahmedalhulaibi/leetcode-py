import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_the_winner, run_find_the_winner
    from solution import Solution

    return Solution, assert_find_the_winner, run_find_the_winner


@app.cell
def _():
    # Example test case
    n = 5
    k = 2
    expected = 3
    return expected, k, n


@app.cell
def _(Solution, k, n, run_find_the_winner):
    result = run_find_the_winner(Solution, n, k)
    result
    return (result,)


@app.cell
def _(assert_find_the_winner, expected, result):
    assert_find_the_winner(result, expected)
    return


if __name__ == "__main__":
    app.run()
