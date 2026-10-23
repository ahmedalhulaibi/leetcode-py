import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_component_size, run_largest_component_size
    from solution import Solution

    return Solution, assert_largest_component_size, run_largest_component_size


@app.cell
def _():
    # Example test case
    nums = [4, 6, 15, 35]
    expected = 4
    return expected, nums


@app.cell
def _(Solution, nums, run_largest_component_size):
    result = run_largest_component_size(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_largest_component_size, expected, result):
    assert_largest_component_size(result, expected)
    return


if __name__ == "__main__":
    app.run()
