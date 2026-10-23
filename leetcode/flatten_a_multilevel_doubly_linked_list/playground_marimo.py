import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_flatten, run_flatten
    from solution import Solution

    return Solution, assert_flatten, run_flatten


@app.cell
def _():
    # Example test case
    head_list: list[int | None] = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12]
    expected_list: list[int | None] = [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]
    return expected_list, head_list


@app.cell
def _(Solution, head_list: list[int | None], run_flatten):
    result = run_flatten(Solution, head_list)
    result
    return (result,)


@app.cell
def _(assert_flatten, expected_list: list[int | None], result):
    assert_flatten(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
