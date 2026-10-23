import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_random_pick_index, run_random_pick_index
    from solution import Solution

    return Solution, assert_random_pick_index, run_random_pick_index


@app.cell
def _():
    # Example test case
    operations = ["Solution", "pick", "pick", "pick"]
    inputs = [[[1, 2, 3, 3, 3]], [3], [1], [3]]
    expected = [[None], [2, 3, 4], [0], [2, 3, 4]]
    return expected, inputs, operations


@app.cell
def _(Solution, inputs, operations, run_random_pick_index):
    result = run_random_pick_index(Solution, operations, inputs)
    print(result)
    result
    return (result,)


@app.cell
def _(assert_random_pick_index, expected, result):
    assert_random_pick_index(result, expected)
    return


if __name__ == "__main__":
    app.run()
