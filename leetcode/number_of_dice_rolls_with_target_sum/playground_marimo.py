import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_rolls_to_target, run_num_rolls_to_target
    from solution import Solution

    return Solution, assert_num_rolls_to_target, run_num_rolls_to_target


@app.cell
def _():
    # Example test case
    n = 2
    k = 6
    target = 7
    expected = 6
    return expected, k, n, target


@app.cell
def _(Solution, k, n, run_num_rolls_to_target, target):
    result = run_num_rolls_to_target(Solution, n, k, target)
    result
    return (result,)


@app.cell
def _(assert_num_rolls_to_target, expected, result):
    assert_num_rolls_to_target(result, expected)
    return


if __name__ == "__main__":
    app.run()
