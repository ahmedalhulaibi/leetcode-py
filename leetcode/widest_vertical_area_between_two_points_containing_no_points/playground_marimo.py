import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_width_of_vertical_area, run_max_width_of_vertical_area
    from solution import Solution

    return (
        Solution,
        assert_max_width_of_vertical_area,
        run_max_width_of_vertical_area,
    )


@app.cell
def _():
    # Example test case
    points: list[list[int]] = [[8, 7], [9, 9], [7, 4], [9, 7]]
    expected: int = 1
    return expected, points


@app.cell
def _(Solution, points: list[list[int]], run_max_width_of_vertical_area):
    result = run_max_width_of_vertical_area(Solution, points)
    result
    return (result,)


@app.cell
def _(assert_max_width_of_vertical_area, expected: int, result):
    assert_max_width_of_vertical_area(result, expected)
    return


if __name__ == "__main__":
    app.run()
