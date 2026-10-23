import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_split_into_fibonacci, run_split_into_fibonacci
    from solution import Solution

    return Solution, assert_split_into_fibonacci, run_split_into_fibonacci


@app.cell
def _():
    # Example test case
    num = "1101111"
    expected = [11, 0, 11, 11]
    return expected, num


@app.cell
def _(Solution, num, run_split_into_fibonacci):
    result = run_split_into_fibonacci(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_split_into_fibonacci, expected, result):
    assert_split_into_fibonacci(result, expected)
    return


if __name__ == "__main__":
    app.run()
