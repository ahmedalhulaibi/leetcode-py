import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_random_pick_operations, run_random_pick_operations
    from solution import Solution

    return Solution, assert_random_pick_operations, run_random_pick_operations


@app.cell
def _():
    # Example test case - single element, deterministic output
    operations = ["Solution", "pickIndex"]
    inputs = [[1], []]
    expected = [None, 0]
    return expected, inputs, operations


@app.cell
def _(Solution, inputs, operations, run_random_pick_operations):
    result = run_random_pick_operations(Solution, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_random_pick_operations, expected, result):
    assert_random_pick_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
