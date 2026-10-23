import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_path_sum, run_path_sum
    from solution import Solution

    return Solution, assert_path_sum, run_path_sum


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    target_sum = 8
    expected = 3
    return expected, root_list, target_sum


@app.cell
def _(Solution, root_list: list[int | None], run_path_sum, target_sum):
    result = run_path_sum(Solution, root_list, target_sum)
    result
    return (result,)


@app.cell
def _(assert_path_sum, expected, result):
    assert_path_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
