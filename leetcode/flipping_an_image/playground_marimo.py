import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_flip_and_invert_image, run_flip_and_invert_image
    from solution import Solution

    return Solution, assert_flip_and_invert_image, run_flip_and_invert_image


@app.cell
def _():
    # Example test case
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    expected = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    return expected, image


@app.cell
def _(Solution, image, run_flip_and_invert_image):
    result = run_flip_and_invert_image(Solution, image)
    result
    return (result,)


@app.cell
def _(assert_flip_and_invert_image, expected, result):
    assert_flip_and_invert_image(result, expected)
    return


if __name__ == "__main__":
    app.run()
