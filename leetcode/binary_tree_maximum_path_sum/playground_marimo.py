import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_path_sum, run_max_path_sum
    from solution import Solution

    return Solution, assert_max_path_sum, run_max_path_sum


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3]
    expected: int = 6
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_max_path_sum):
    result = run_max_path_sum(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_max_path_sum, expected: int, result):
    assert_max_path_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
