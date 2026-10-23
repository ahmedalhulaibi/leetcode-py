import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_diameter, run_diameter
    from solution import Solution

    return Solution, assert_diameter, run_diameter


@app.cell
def _():
    # Example test case
    root_list: list[int | None] = [1, None, 3, 2, 4, None, 5, 6]
    expected = 3
    return expected, root_list


@app.cell
def _(Solution, root_list: list[int | None], run_diameter):
    result = run_diameter(Solution, root_list)
    result
    return (result,)


@app.cell
def _(assert_diameter, expected, result):
    assert_diameter(result, expected)
    return


if __name__ == "__main__":
    app.run()
