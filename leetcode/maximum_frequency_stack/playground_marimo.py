import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_freq_stack_operations, run_freq_stack_operations
    from solution import FreqStack

    return FreqStack, assert_freq_stack_operations, run_freq_stack_operations


@app.cell
def _():
    # Example test case
    operations = [
        "FreqStack",
        "push",
        "push",
        "push",
        "push",
        "push",
        "push",
        "pop",
        "pop",
        "pop",
        "pop",
    ]
    inputs = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
    expected = [None, None, None, None, None, None, None, 5, 7, 5, 4]
    return expected, inputs, operations


@app.cell
def _(FreqStack, inputs, operations, run_freq_stack_operations):
    result = run_freq_stack_operations(FreqStack, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_freq_stack_operations, expected, result):
    assert_freq_stack_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
