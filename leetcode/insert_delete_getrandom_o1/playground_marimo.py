import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_randomized_set_operations, run_randomized_set_operations
    from solution import RandomizedSet

    return (
        RandomizedSet,
        assert_randomized_set_operations,
        run_randomized_set_operations,
    )


@app.cell
def _():
    # Example test case
    operations = ["RandomizedSet", "insert", "getRandom"]
    inputs = [[], [5], []]
    expected = [None, True, 5]
    return expected, inputs, operations


@app.cell
def _(RandomizedSet, inputs, operations, run_randomized_set_operations):
    result = run_randomized_set_operations(RandomizedSet, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_randomized_set_operations, expected, result):
    assert_randomized_set_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
