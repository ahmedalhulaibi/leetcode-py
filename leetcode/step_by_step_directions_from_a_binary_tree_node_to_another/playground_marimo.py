import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_directions, run_get_directions
    from solution import Solution

    return Solution, assert_get_directions, run_get_directions


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [5, 1, 2, 3, None, 6, 4]
    start_value = 3
    dest_value = 6
    expected = "UURL"
    return dest_value, expected, root_list, start_value


@app.cell
def _(
    Solution,
    dest_value,
    root_list: list[int | None],
    run_get_directions,
    start_value,
):
    result = run_get_directions(Solution, root_list, start_value, dest_value)
    result
    return (result,)


@app.cell
def _(assert_get_directions, expected, result):
    assert_get_directions(result, expected)
    return


if __name__ == "__main__":
    app.run()
