import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_image_smoother, run_image_smoother
    from solution import Solution

    return Solution, assert_image_smoother, run_image_smoother


@app.cell
def _():
    # Example test case
    img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return expected, img


@app.cell
def _(Solution, img, run_image_smoother):
    result = run_image_smoother(Solution, img)
    result
    return (result,)


@app.cell
def _(assert_image_smoother, expected, result):
    assert_image_smoother(result, expected)
    return


if __name__ == "__main__":
    app.run()
