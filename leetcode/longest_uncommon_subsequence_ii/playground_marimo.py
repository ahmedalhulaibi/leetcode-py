import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_lus_length, run_find_lus_length
    from solution import Solution

    return Solution, assert_find_lus_length, run_find_lus_length


@app.cell
def _():
    # Example test case
    strs = ["aba", "cdc", "eae"]
    expected = 3
    return expected, strs


@app.cell
def _(Solution, run_find_lus_length, strs):
    result = run_find_lus_length(Solution, strs)
    result
    return (result,)


@app.cell
def _(assert_find_lus_length, expected, result):
    assert_find_lus_length(result, expected)
    return


if __name__ == "__main__":
    app.run()
