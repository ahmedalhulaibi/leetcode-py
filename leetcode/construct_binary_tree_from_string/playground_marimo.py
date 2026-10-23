import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_str2tree, run_str2tree
    from solution import Solution

    return Solution, assert_str2tree, run_str2tree


@app.cell
def _():
    # Example test case
    s = "4(2(3)(1))(6(5))"
    expected_list: list[int | None] = [4, 2, 6, 3, 1, 5]
    return expected_list, s


@app.cell
def _(Solution, run_str2tree, s):
    result = run_str2tree(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_str2tree, expected_list: list[int | None], result):
    assert_str2tree(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
