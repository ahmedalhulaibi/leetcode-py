import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_deletion_size, run_min_deletion_size
    from solution import Solution

    return Solution, assert_min_deletion_size, run_min_deletion_size


@app.cell
def _():
    # Example test case
    strs = ["babca", "bbazb"]
    expected = 3
    return expected, strs


@app.cell
def _(Solution, run_min_deletion_size, strs):
    result = run_min_deletion_size(Solution, strs)
    result
    return (result,)


@app.cell
def _(assert_min_deletion_size, expected, result):
    assert_min_deletion_size(result, expected)
    return


if __name__ == "__main__":
    app.run()
