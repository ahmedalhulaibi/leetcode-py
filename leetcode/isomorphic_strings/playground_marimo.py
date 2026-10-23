import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_isomorphic, run_is_isomorphic
    from solution import Solution

    return Solution, assert_is_isomorphic, run_is_isomorphic


@app.cell
def _():
    # Example test case
    s = "egg"
    t = "add"
    expected = True
    return expected, s, t


@app.cell
def _(Solution, run_is_isomorphic, s, t):
    result = run_is_isomorphic(Solution, s, t)
    result
    return (result,)


@app.cell
def _(assert_is_isomorphic, expected, result):
    assert_is_isomorphic(result, expected)
    return


if __name__ == "__main__":
    app.run()
