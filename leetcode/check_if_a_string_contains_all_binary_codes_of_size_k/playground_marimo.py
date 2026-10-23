import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_has_all_codes, run_has_all_codes
    from solution import Solution

    return Solution, assert_has_all_codes, run_has_all_codes


@app.cell
def _():
    # Example test case
    s = "00110110"
    k = 2
    expected = True
    return expected, k, s


@app.cell
def _(Solution, k, run_has_all_codes, s):
    result = run_has_all_codes(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_has_all_codes, expected, result):
    assert_has_all_codes(result, expected)
    return


if __name__ == "__main__":
    app.run()
