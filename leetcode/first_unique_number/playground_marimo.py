import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_first_unique, run_first_unique
    from solution import FirstUnique

    return FirstUnique, assert_first_unique, run_first_unique


@app.cell
def _():
    # Example test case
    operations = [
        "FirstUnique",
        "show_first_unique",
        "add",
        "show_first_unique",
        "add",
        "show_first_unique",
        "add",
        "show_first_unique",
    ]
    inputs = [[2, 3, 5], [], [5], [], [2], [], [3], []]
    expected = [None, 2, None, 2, None, 3, None, -1]
    return expected, inputs, operations


@app.cell
def _(FirstUnique, inputs, operations, run_first_unique):
    result, first_unique = run_first_unique(FirstUnique, operations, inputs)
    print(result)
    first_unique
    return (result,)


@app.cell
def _(assert_first_unique, expected, result):
    assert_first_unique(result, expected)
    return


if __name__ == "__main__":
    app.run()
