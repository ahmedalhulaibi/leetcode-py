import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_second_minimum_value, run_find_second_minimum_value
    from solution import Solution

    return (
        Solution,
        assert_find_second_minimum_value,
        run_find_second_minimum_value,
    )


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [2, 2, 5, None, None, 5, 7]
    expected = 5
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_find_second_minimum_value):
    result = run_find_second_minimum_value(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_find_second_minimum_value, expected, result):
    assert_find_second_minimum_value(result, expected)
    return


if __name__ == "__main__":
    app.run()
