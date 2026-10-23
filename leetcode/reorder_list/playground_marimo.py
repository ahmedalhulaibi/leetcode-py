import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_reorder_list, run_reorder_list
    from solution import Solution

    return Solution, assert_reorder_list, run_reorder_list


@app.cell
def _():
    # Example test case
    head_list: list[int] = [1, 2, 3, 4]
    expected: list[int] = [1, 4, 2, 3]
    return expected, head_list


@app.cell
def _(Solution, head_list: list[int], run_reorder_list):
    result = run_reorder_list(Solution, head_list)
    result
    return (result,)


@app.cell
def _(assert_reorder_list, expected: list[int], result):
    assert_reorder_list(result, expected)
    return


if __name__ == "__main__":
    app.run()
