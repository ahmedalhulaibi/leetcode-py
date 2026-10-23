import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reorganize_string, run_reorganize_string
    from solution import Solution

    return Solution, assert_reorganize_string, run_reorganize_string


@app.cell
def _():
    # Example test case
    s = "aab"
    expected = "aba"
    return (s,)


@app.cell
def _(Solution, run_reorganize_string, s):
    result = run_reorganize_string(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_reorganize_string, result, s):
    assert_reorganize_string(result, s)
    return


if __name__ == "__main__":
    app.run()
