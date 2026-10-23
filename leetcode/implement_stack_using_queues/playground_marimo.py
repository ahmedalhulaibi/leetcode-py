import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_my_stack, run_my_stack
    from solution import MyStack

    return MyStack, assert_my_stack, run_my_stack


@app.cell
def _():
    # Example test case
    operations = ["MyStack", "push", "push", "top", "pop", "empty"]
    inputs = [[], [1], [2], [], [], []]
    expected = [None, None, None, 2, 2, False]
    return expected, inputs, operations


@app.cell
def _(MyStack, inputs, operations, run_my_stack):
    result, stack = run_my_stack(MyStack, operations, inputs)
    print(result)
    stack
    return (result,)


@app.cell
def _(assert_my_stack, expected, result):
    assert_my_stack(result, expected)
    return


if __name__ == "__main__":
    app.run()
