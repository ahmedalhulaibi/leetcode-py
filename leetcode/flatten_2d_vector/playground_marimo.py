import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_flatten_2d_vector, run_flatten_2d_vector
    from solution import Vector2D

    return Vector2D, assert_flatten_2d_vector, run_flatten_2d_vector


@app.cell
def _():
    # Example test case
    operations = ["Vector2D", "next", "next", "next", "has_next"]
    inputs = [[[1, 2], [3], [4]], [], [], [], []]
    expected = [None, 1, 2, 3, True]
    return expected, inputs, operations


@app.cell
def _(Vector2D, inputs, operations, run_flatten_2d_vector):
    result, iterator = run_flatten_2d_vector(Vector2D, operations, inputs)
    print(result)
    iterator
    return (result,)


@app.cell
def _(assert_flatten_2d_vector, expected, result):
    assert_flatten_2d_vector(result, expected)
    return


if __name__ == "__main__":
    app.run()
