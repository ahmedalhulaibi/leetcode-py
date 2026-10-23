import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_one_edit_distance, run_is_one_edit_distance
    from solution import Solution

    return Solution, assert_is_one_edit_distance, run_is_one_edit_distance


@app.cell
def _():
    # Example test case
    s = "ab"
    t = "acb"
    expected = True
    return expected, s, t


@app.cell
def _(Solution, run_is_one_edit_distance, s, t):
    result = run_is_one_edit_distance(Solution, s, t)
    result
    return (result,)


@app.cell
def _(assert_is_one_edit_distance, expected, result):
    assert_is_one_edit_distance(result, expected)
    return


if __name__ == "__main__":
    app.run()
