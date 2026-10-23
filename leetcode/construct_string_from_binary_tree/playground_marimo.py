import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_tree2str, run_tree2str
    from solution import Solution

    return Solution, assert_tree2str, run_tree2str


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3, 4]
    expected = "1(2(4))(3)"
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_tree2str):
    result = run_tree2str(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_tree2str, expected, result):
    assert_tree2str(result, expected)
    return


if __name__ == "__main__":
    app.run()
