import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_traverse_all_pairs, run_can_traverse_all_pairs
    from solution import Solution

    return Solution, assert_can_traverse_all_pairs, run_can_traverse_all_pairs


@app.cell
def _():
    # Example test case
    nums = [2, 3, 6]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_can_traverse_all_pairs):
    result = run_can_traverse_all_pairs(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_can_traverse_all_pairs, expected, result):
    assert_can_traverse_all_pairs(result, expected)
    return


if __name__ == "__main__":
    app.run()
