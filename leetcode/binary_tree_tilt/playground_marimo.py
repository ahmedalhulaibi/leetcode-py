import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_tilt, run_find_tilt
    from solution import Solution

    return Solution, assert_find_tilt, run_find_tilt


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, 2, 3]
    expected = 1
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_find_tilt):
    result = run_find_tilt(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_find_tilt, expected, result):
    assert_find_tilt(result, expected)
    return


if __name__ == "__main__":
    app.run()
