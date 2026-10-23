import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_components, run_num_components
    from solution import Solution

    return Solution, assert_num_components, run_num_components


@app.cell
def _():
    # Example test case
    head_vals: list[int] = [0, 1, 2, 3]
    nums: list[int] = [0, 1, 3]
    expected = 2
    return expected, head_vals, nums


@app.cell
def _(Solution, head_vals: list[int], nums: list[int], run_num_components):
    result = run_num_components(Solution, head_vals, nums)
    result
    return (result,)


@app.cell
def _(assert_num_components, expected, result):
    assert_num_components(result, expected)
    return


if __name__ == "__main__":
    app.run()
