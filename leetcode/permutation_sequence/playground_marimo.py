import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_permutation, run_get_permutation
    from solution import Solution

    return Solution, assert_get_permutation, run_get_permutation


@app.cell
def _():
    # Example test case
    n = 3
    k = 3
    expected = "213"
    return expected, k, n


@app.cell
def _(Solution, k, n, run_get_permutation):
    result = run_get_permutation(Solution, n, k)
    result
    return (result,)


@app.cell
def _(assert_get_permutation, expected, result):
    assert_get_permutation(result, expected)
    return


if __name__ == "__main__":
    app.run()
