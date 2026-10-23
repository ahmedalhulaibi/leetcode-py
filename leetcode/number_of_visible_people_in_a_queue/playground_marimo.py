import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_see_persons_count, run_can_see_persons_count
    from solution import Solution

    return Solution, assert_can_see_persons_count, run_can_see_persons_count


@app.cell
def _():
    # Example test case
    heights = [10, 6, 8, 5, 11, 9]
    expected = [3, 1, 2, 1, 1, 0]
    return expected, heights


@app.cell
def _(Solution, heights, run_can_see_persons_count):
    result = run_can_see_persons_count(Solution, heights)
    result
    return (result,)


@app.cell
def _(assert_can_see_persons_count, expected, result):
    assert_can_see_persons_count(result, expected)
    return


if __name__ == "__main__":
    app.run()
