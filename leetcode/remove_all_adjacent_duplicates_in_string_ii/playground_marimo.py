import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_duplicates, run_remove_duplicates
    from solution import Solution

    return Solution, assert_remove_duplicates, run_remove_duplicates


@app.cell
def _():
    # Example test case
    s = "deeedbbcccbdaa"
    k = 3
    expected = "aa"
    return expected, k, s


@app.cell
def _(Solution, k, run_remove_duplicates, s):
    result = run_remove_duplicates(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_remove_duplicates, expected, result):
    assert_remove_duplicates(result, expected)
    return


if __name__ == "__main__":
    app.run()
