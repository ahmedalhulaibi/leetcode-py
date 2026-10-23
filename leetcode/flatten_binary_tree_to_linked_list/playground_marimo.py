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
    root_list: list[int | None] = [1, 2, 5, 3, 4, None, 6]
    expected = [1, None, 2, None, 3, None, 4, None, 5, None, 6]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_flatten):
    result = run_flatten(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_flatten, expected, result):
    assert_flatten(result, expected)
    return


if __name__ == "__main__":
    app.run()
