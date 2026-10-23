import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_most_profitable_path, run_most_profitable_path
    from solution import Solution

    return Solution, assert_most_profitable_path, run_most_profitable_path


@app.cell
def _():
    # Example test case
    edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
    bob = 3
    amount = [-2, 4, 2, -4, 6]
    expected = 6
    return amount, bob, edges, expected


@app.cell
def _(Solution, amount, bob, edges, run_most_profitable_path):
    result = run_most_profitable_path(Solution, edges, bob, amount)
    result
    return (result,)


@app.cell
def _(assert_most_profitable_path, expected, result):
    assert_most_profitable_path(result, expected)
    return


if __name__ == "__main__":
    app.run()
