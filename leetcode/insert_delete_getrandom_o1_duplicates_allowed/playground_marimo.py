import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_randomized_collection_operations, run_randomized_collection_operations
    from solution import RandomizedCollection

    return (
        RandomizedCollection,
        assert_randomized_collection_operations,
        run_randomized_collection_operations,
    )


@app.cell
def _():
    # Example test case
    operations = [
        "RandomizedCollection",
        "insert",
        "insert",
        "insert",
        "getRandom",
        "remove",
        "getRandom",
    ]
    inputs = [[], [1], [1], [1], [], [1], []]
    expected = [None, True, False, False, 1, True, 1]
    return expected, inputs, operations


@app.cell
def _(
    RandomizedCollection,
    inputs,
    operations,
    run_randomized_collection_operations,
):
    result = run_randomized_collection_operations(RandomizedCollection, operations, inputs)
    result
    return (result,)


@app.cell
def _(assert_randomized_collection_operations, expected, result):
    assert_randomized_collection_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
