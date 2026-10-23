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
    root_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    target_sum = 22
    expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
    return expected, root_list, target_sum


@app.cell
def _(Solution, root_list, run_path_sum, target_sum):
    result = run_path_sum(Solution, root_list, target_sum)
    result
    return (result,)


@app.cell
def _(assert_path_sum, expected, result):
    assert_path_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
