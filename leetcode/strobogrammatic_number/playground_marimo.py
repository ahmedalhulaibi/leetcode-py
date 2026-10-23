import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_strobogrammatic, run_is_strobogrammatic
    from solution import Solution

    return Solution, assert_is_strobogrammatic, run_is_strobogrammatic


@app.cell
def _():
    # Example test case
    num = "69"
    expected = True
    return expected, num


@app.cell
def _(Solution, num, run_is_strobogrammatic):
    result = run_is_strobogrammatic(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_is_strobogrammatic, expected, result):
    assert_is_strobogrammatic(result, expected)
    return


if __name__ == "__main__":
    app.run()
