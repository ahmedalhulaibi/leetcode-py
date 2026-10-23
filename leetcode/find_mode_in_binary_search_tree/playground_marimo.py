import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_mode, run_find_mode
    from solution import Solution

    return Solution, assert_find_mode, run_find_mode


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, None, 2, 2]
    expected: list[int] = [2]
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_find_mode):
    result = run_find_mode(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_find_mode, expected: list[int], result):
    assert_find_mode(result, expected)
    return


if __name__ == "__main__":
    app.run()
