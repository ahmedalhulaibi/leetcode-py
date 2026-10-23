import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_closest_value, run_closest_value
    from solution import Solution

    return Solution, assert_closest_value, run_closest_value


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [4, 2, 5, 1, 3]
    target = 3.714286
    expected = 4
    return expected, root_list, target


@app.cell
def _(Solution, root_list: list[int | None], run_closest_value, target):
    result = run_closest_value(Solution, root_list, target)
    result
    return (result,)


@app.cell
def _(assert_closest_value, expected, result):
    assert_closest_value(result, expected)
    return


if __name__ == "__main__":
    app.run()
