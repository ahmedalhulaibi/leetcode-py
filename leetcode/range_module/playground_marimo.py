import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_range_module, run_range_module
    from solution import RangeModule

    return RangeModule, assert_range_module, run_range_module


@app.cell
def _():
    # Example test case
    operations = ["RangeModule", "add_range", "remove_range", "query_range", "query_range"]
    inputs = [[], [10, 20], [14, 16], [10, 14], [13, 15]]
    expected = [None, None, None, True, False]
    return expected, inputs, operations


@app.cell
def _(RangeModule, inputs, operations, run_range_module):
    result, module = run_range_module(RangeModule, operations, inputs)
    print(result)
    module
    return (result,)


@app.cell
def _(assert_range_module, expected, result):
    assert_range_module(result, expected)
    return


if __name__ == "__main__":
    app.run()
