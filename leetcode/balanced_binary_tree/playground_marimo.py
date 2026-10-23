import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_balanced, run_is_balanced
    from solution import Solution

    return Solution, assert_is_balanced, run_is_balanced


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
    expected = True
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_is_balanced):
    result = run_is_balanced(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_is_balanced, expected, result):
    assert_is_balanced(result, expected)
    return


if __name__ == "__main__":
    app.run()
