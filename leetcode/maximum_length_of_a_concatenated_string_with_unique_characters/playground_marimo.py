import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_len, run_max_len
    from solution import Solution

    return Solution, assert_max_len, run_max_len


@app.cell
def _():
    # Example test case
    arr = ["un", "iq", "ue"]
    expected = 4
    return arr, expected


@app.cell
def _(Solution, arr, run_max_len):
    result = run_max_len(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_max_len, expected, result):
    assert_max_len(result, expected)
    return


if __name__ == "__main__":
    app.run()
