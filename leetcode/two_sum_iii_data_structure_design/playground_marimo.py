import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_two_sum, run_two_sum
    from solution import TwoSum

    return TwoSum, assert_two_sum, run_two_sum


@app.cell
def _():
    # Example test case
    operations = ["TwoSum", "add", "add", "add", "find", "find"]
    inputs = [[], [1], [3], [5], [4], [7]]
    expected = [None, None, None, None, True, False]
    return expected, inputs, operations


@app.cell
def _(TwoSum, inputs, operations, run_two_sum):
    result, two_sum = run_two_sum(TwoSum, operations, inputs)
    print(result)
    two_sum
    return (result,)


@app.cell
def _(assert_two_sum, expected, result):
    assert_two_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
