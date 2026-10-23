import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_closest_leaf, run_find_closest_leaf
    from solution import Solution

    return Solution, assert_find_closest_leaf, run_find_closest_leaf


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3, 4, None, None, None, 5, None, 6]
    k = 2
    expected = 3
    return expected, k, root_list


@app.cell
def _(Solution, k, root_list: list[int | None], run_find_closest_leaf):
    result = run_find_closest_leaf(Solution, root_list, k)
    result
    return (result,)


@app.cell
def _(assert_find_closest_leaf, expected, result):
    assert_find_closest_leaf(result, expected)
    return


if __name__ == "__main__":
    app.run()
