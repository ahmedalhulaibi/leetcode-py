import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from typing import Any

    from helpers import assert_depth_sum_inverse, run_depth_sum_inverse
    from solution import Solution

    return Any, Solution, assert_depth_sum_inverse, run_depth_sum_inverse


@app.cell
def _(Any):
    # Example test case
    nested_list: list[Any] = [[1, 1], 2, [1, 1]]
    expected = 8
    return expected, nested_list


@app.cell
def _(Solution, nested_list: "list[Any]", run_depth_sum_inverse):
    result = run_depth_sum_inverse(Solution, nested_list)
    result
    return (result,)


@app.cell
def _(assert_depth_sum_inverse, expected, result):
    assert_depth_sum_inverse(result, expected)
    return


if __name__ == "__main__":
    app.run()
