import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_permutation, run_find_permutation
    from solution import Solution

    return Solution, assert_find_permutation, run_find_permutation


@app.cell
def _():
    # Example test case
    s = "DI"
    expected = [2, 1, 3]
    return expected, s


@app.cell
def _(Solution, run_find_permutation, s):
    result = run_find_permutation(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_find_permutation, expected, result):
    assert_find_permutation(result, expected)
    return


if __name__ == "__main__":
    app.run()
