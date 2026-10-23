import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_recolors, run_minimum_recolors
    from solution import Solution

    return Solution, assert_minimum_recolors, run_minimum_recolors


@app.cell
def _():
    # Example test case
    blocks = "WBBWWBBWBW"
    k = 7
    expected = 3
    return blocks, expected, k


@app.cell
def _(Solution, blocks, k, run_minimum_recolors):
    result = run_minimum_recolors(Solution, blocks, k)
    result
    return (result,)


@app.cell
def _(assert_minimum_recolors, expected, result):
    assert_minimum_recolors(result, expected)
    return


if __name__ == "__main__":
    app.run()
