import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_stack, run_max_stack
    from solution import MaxStack

    return MaxStack, assert_max_stack, run_max_stack


@app.cell
def _():
    # Example test case
    operations = ["MaxStack", "push", "push", "push", "top", "pop_max", "top", "peek_max", "pop", "top"]
    inputs = [[], [5], [1], [5], [], [], [], [], [], []]
    expected = [None, None, None, None, 5, 5, 1, 5, 1, 5]
    return expected, inputs, operations


@app.cell
def _(MaxStack, inputs, operations, run_max_stack):
    result, stack = run_max_stack(MaxStack, operations, inputs)
    print(result)
    stack
    return (result,)


@app.cell
def _(assert_max_stack, expected, result):
    assert_max_stack(result, expected)
    return


if __name__ == "__main__":
    app.run()
