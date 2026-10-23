import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_boxes_in_warehouse, run_max_boxes_in_warehouse
    from solution import Solution

    return Solution, assert_max_boxes_in_warehouse, run_max_boxes_in_warehouse


@app.cell
def _():
    # Example test case
    boxes = [4, 3, 4, 1]
    warehouse = [5, 3, 3, 4, 1]
    expected = 3
    return boxes, expected, warehouse


@app.cell
def _(Solution, boxes, run_max_boxes_in_warehouse, warehouse):
    result = run_max_boxes_in_warehouse(Solution, boxes, warehouse)
    result
    return (result,)


@app.cell
def _(assert_max_boxes_in_warehouse, expected, result):
    assert_max_boxes_in_warehouse(result, expected)
    return


if __name__ == "__main__":
    app.run()
