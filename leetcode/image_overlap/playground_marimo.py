import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_overlap, run_largest_overlap
    from solution import Solution

    return Solution, assert_largest_overlap, run_largest_overlap


@app.cell
def _():
    # Example test case
    img1 = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
    img2 = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
    expected = 3
    return expected, img1, img2


@app.cell
def _(Solution, img1, img2, run_largest_overlap):
    result = run_largest_overlap(Solution, img1, img2)
    result
    return (result,)


@app.cell
def _(assert_largest_overlap, expected, result):
    assert_largest_overlap(result, expected)
    return


if __name__ == "__main__":
    app.run()
