import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_stack_operations, run_min_stack_operations
    from solution import MinStack

    return MinStack, assert_min_stack_operations, run_min_stack_operations


@app.cell
def _():
    # Example test case
    operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    inputs = [[], [-2], [0], [-3], [], [], [], []]
    expected = [None, None, None, None, -3, None, 0, -2]
    return expected, inputs, operations


@app.cell
def _(MinStack, inputs, operations, run_min_stack_operations):
    result = run_min_stack_operations(MinStack, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_min_stack_operations, expected, result):
    assert_min_stack_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
