import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_root, run_find_root
    from solution import Solution

    return Solution, assert_find_root, run_find_root


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, None, 3, 2, 4, None, 5, 6]
    return (root_list,)


@app.cell
def _(Solution, root_list: list[int | None], run_find_root):
    result = run_find_root(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_find_root, result, root_list: list[int | None]):
    assert_find_root(result, root_list)
    return


if __name__ == "__main__":
    app.run()
