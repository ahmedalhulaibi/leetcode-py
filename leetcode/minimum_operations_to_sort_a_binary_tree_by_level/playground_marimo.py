import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_operations, run_minimum_operations
    from solution import Solution

    return Solution, assert_minimum_operations, run_minimum_operations


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10]
    expected = 3
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_minimum_operations):
    result = run_minimum_operations(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_minimum_operations, expected, result):
    assert_minimum_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
