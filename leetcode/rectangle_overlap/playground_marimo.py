import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_rectangle_overlap, run_is_rectangle_overlap
    from solution import Solution

    return Solution, assert_is_rectangle_overlap, run_is_rectangle_overlap


@app.cell
def _():
    # Example test case
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    expected = True
    return expected, rec1, rec2


@app.cell
def _(Solution, rec1, rec2, run_is_rectangle_overlap):
    result = run_is_rectangle_overlap(Solution, rec1, rec2)
    result
    return (result,)


@app.cell
def _(assert_is_rectangle_overlap, expected, result):
    assert_is_rectangle_overlap(result, expected)
    return


if __name__ == "__main__":
    app.run()
