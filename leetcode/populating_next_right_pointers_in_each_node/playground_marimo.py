import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_connect, run_connect
    from solution import Solution

    return Solution, assert_connect, run_connect


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3, 4, 5, 6, 7]
    expected_list: list[int | None] = [1, None, 2, 3, None, 4, 5, 6, 7, None]
    return expected_list, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_connect):
    result = run_connect(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_connect, expected_list: list[int | None], result):
    assert_connect(result, expected_list)
    return


if __name__ == "__main__":
    app.run()
