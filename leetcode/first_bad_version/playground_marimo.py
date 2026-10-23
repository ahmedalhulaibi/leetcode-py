import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_first_bad_version, run_first_bad_version
    from solution import Solution

    return Solution, assert_first_bad_version, run_first_bad_version


@app.cell
def _():
    # Example test case
    n = 5
    bad = 4
    expected = 4
    return bad, expected, n


@app.cell
def _(Solution, bad, n, run_first_bad_version):
    result = run_first_bad_version(Solution, n, bad)
    result
    return (result,)


@app.cell
def _(assert_first_bad_version, expected, result):
    assert_first_bad_version(result, expected)
    return


if __name__ == "__main__":
    app.run()
