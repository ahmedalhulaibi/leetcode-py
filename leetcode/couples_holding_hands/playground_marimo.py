import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_swaps_couples, run_min_swaps_couples
    from solution import Solution

    return Solution, assert_min_swaps_couples, run_min_swaps_couples


@app.cell
def _():
    # Example test case
    row: list[int] = [0, 2, 1, 3]
    expected = 1
    return expected, row


@app.cell
def _(Solution, row: list[int], run_min_swaps_couples):
    result = run_min_swaps_couples(Solution, row)
    result
    return (result,)


@app.cell
def _(assert_min_swaps_couples, expected, result):
    assert_min_swaps_couples(result, expected)
    return


if __name__ == "__main__":
    app.run()
