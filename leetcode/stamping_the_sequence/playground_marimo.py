import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_moves_to_stamp, run_moves_to_stamp
    from solution import Solution

    return Solution, assert_moves_to_stamp, run_moves_to_stamp


@app.cell
def _():
    # Example test case
    stamp = "abc"
    target = "ababc"
    expected = [0, 2]
    return expected, stamp, target


@app.cell
def _(Solution, run_moves_to_stamp, stamp, target):
    result = run_moves_to_stamp(Solution, stamp, target)
    result
    return (result,)


@app.cell
def _(assert_moves_to_stamp, expected, result, stamp, target):
    assert_moves_to_stamp(result, expected, stamp, target)
    return


if __name__ == "__main__":
    app.run()
