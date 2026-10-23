import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_interchangeable_rectangles, run_interchangeable_rectangles
    from solution import Solution

    return (
        Solution,
        assert_interchangeable_rectangles,
        run_interchangeable_rectangles,
    )


@app.cell
def _():
    # Example test case
    rectangles: list[list[int]] = [[4, 8], [3, 6], [10, 20], [15, 30]]
    expected = 6
    return expected, rectangles


@app.cell
def _(Solution, rectangles: list[list[int]], run_interchangeable_rectangles):
    result = run_interchangeable_rectangles(Solution, rectangles)
    result
    return (result,)


@app.cell
def _(assert_interchangeable_rectangles, expected, result):
    assert_interchangeable_rectangles(result, expected)
    return


if __name__ == "__main__":
    app.run()
