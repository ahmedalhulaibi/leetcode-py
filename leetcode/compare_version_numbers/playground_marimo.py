import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_compare_version, run_compare_version
    from solution import Solution

    return Solution, assert_compare_version, run_compare_version


@app.cell
def _():
    # Example test case
    version1 = "1.01"
    version2 = "1.001"
    expected = 0
    return expected, version1, version2


@app.cell
def _(Solution, run_compare_version, version1, version2):
    result = run_compare_version(Solution, version1, version2)
    result
    return (result,)


@app.cell
def _(assert_compare_version, expected, result):
    assert_compare_version(result, expected)
    return


if __name__ == "__main__":
    app.run()
