import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_remove_boxes, run_remove_boxes
    from solution import Solution

    return Solution, assert_remove_boxes, run_remove_boxes


@app.cell
def _():
    # Example test case
    boxes: list[int] = [1, 3, 2, 2, 2, 3, 4, 3, 1]
    expected = 23
    return boxes, expected


@app.cell
def _(Solution, boxes: list[int], run_remove_boxes):
    result = run_remove_boxes(Solution, boxes)
    result
    return (result,)


@app.cell
def _(assert_remove_boxes, expected, result):
    assert_remove_boxes(result, expected)
    return


if __name__ == "__main__":
    app.run()
