import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_transform, run_can_transform
    from solution import Solution

    return Solution, assert_can_transform, run_can_transform


@app.cell
def _():
    # Example test case
    start = "RXXLRXRXL"
    result = "XRLXXRRLX"
    expected = True
    return expected, result, start


@app.cell
def _(Solution, result, run_can_transform, start):
    result_1 = run_can_transform(Solution, start, result)
    result_1
    return (result_1,)


@app.cell
def _(assert_can_transform, expected, result_1):
    assert_can_transform(result_1, expected)
    return


if __name__ == "__main__":
    app.run()
