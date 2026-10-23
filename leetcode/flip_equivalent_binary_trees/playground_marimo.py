import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_flip_equiv, run_flip_equiv
    from solution import Solution

    return Solution, assert_flip_equiv, run_flip_equiv


@app.cell
def _():
    # Example test case
    root1_list: list[int | None] = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8]
    root2_list: list[int | None] = [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]
    expected = True
    return expected, root1_list, root2_list


@app.cell
def _(
    Solution,
    root1_list: list[int | None],
    root2_list: list[int | None],
    run_flip_equiv,
):
    result = run_flip_equiv(Solution, root1_list, root2_list)
    result
    return (result,)


@app.cell
def _(assert_flip_equiv, expected, result):
    assert_flip_equiv(result, expected)
    return


if __name__ == "__main__":
    app.run()
