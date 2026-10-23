import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_depth_sum, run_depth_sum
    from solution import Solution

    return Solution, assert_depth_sum, run_depth_sum


@app.cell
def _():
    # Example test case
    nested_list = [[1, 1], 2, [1, 1]]
    expected = 10
    return expected, nested_list


@app.cell
def _(Solution, nested_list, run_depth_sum):
    result = run_depth_sum(Solution, nested_list)
    result
    return (result,)


@app.cell
def _(assert_depth_sum, expected, result):
    assert_depth_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
