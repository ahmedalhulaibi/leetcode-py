import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_k_closest, run_k_closest
    from solution import Solution

    return Solution, assert_k_closest, run_k_closest


@app.cell
def _():
    # Example test case
    points = [[1, 3], [-2, 2]]
    k = 1
    expected = [[-2, 2]]
    return expected, k, points


@app.cell
def _(Solution, k, points, run_k_closest):
    result = run_k_closest(Solution, points, k)
    result
    return (result,)


@app.cell
def _(assert_k_closest, expected, result):
    assert_k_closest(result, expected)
    return


if __name__ == "__main__":
    app.run()
