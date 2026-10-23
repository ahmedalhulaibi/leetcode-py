import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_to_hex, run_to_hex
    from solution import Solution

    return Solution, assert_to_hex, run_to_hex


@app.cell
def _():
    # Example test case
    num = 26
    expected = "1a"
    return expected, num


@app.cell
def _(Solution, num, run_to_hex):
    result = run_to_hex(Solution, num)
    result
    return (result,)


@app.cell
def _(assert_to_hex, expected, result):
    assert_to_hex(result, expected)
    return


if __name__ == "__main__":
    app.run()
