import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_put_marbles, run_put_marbles
    from solution import Solution

    return Solution, assert_put_marbles, run_put_marbles


@app.cell
def _():
    # Example test case
    weights: list[int] = [1, 3, 5, 1]
    k = 2
    expected = 4
    return expected, k, weights


@app.cell
def _(Solution, k, run_put_marbles, weights: list[int]):
    result = run_put_marbles(Solution, weights, k)
    result
    return (result,)


@app.cell
def _(assert_put_marbles, expected, result):
    assert_put_marbles(result, expected)
    return


if __name__ == "__main__":
    app.run()
