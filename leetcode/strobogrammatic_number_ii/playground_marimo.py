import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_strobogrammatic, run_find_strobogrammatic
    from solution import Solution

    return Solution, assert_find_strobogrammatic, run_find_strobogrammatic


@app.cell
def _():
    # Example test case
    n = 2
    expected = ["11", "69", "88", "96"]
    return expected, n


@app.cell
def _(Solution, n, run_find_strobogrammatic):
    result = run_find_strobogrammatic(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_find_strobogrammatic, expected, result):
    assert_find_strobogrammatic(result, expected)
    return


if __name__ == "__main__":
    app.run()
