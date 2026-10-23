import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_target, run_find_target
    from solution import Solution

    return Solution, assert_find_target, run_find_target


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [5, 3, 6, 2, 4, None, 7]
    k = 9
    expected = True
    return expected, k, root_list


@app.cell
def _(Solution, k, root_list: list[int | None], run_find_target):
    result = run_find_target(Solution, root_list, k)
    result
    return (result,)


@app.cell
def _(assert_find_target, expected, result):
    assert_find_target(result, expected)
    return


if __name__ == "__main__":
    app.run()
