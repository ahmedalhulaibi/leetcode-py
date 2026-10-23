import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_symmetric, run_is_symmetric
    from solution import Solution

    return Solution, assert_is_symmetric, run_is_symmetric


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 2, 3, 4, 4, 3]
    expected = True
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_is_symmetric):
    result = run_is_symmetric(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_is_symmetric, expected, result):
    assert_is_symmetric(result, expected)
    return


if __name__ == "__main__":
    app.run()
