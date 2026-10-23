import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_license_key_formatting, run_license_key_formatting
    from solution import Solution

    return Solution, assert_license_key_formatting, run_license_key_formatting


@app.cell
def _():
    # Example test case
    s = "5F3Z-2e-9-w"
    k = 4
    expected = "5F3Z-2E9W"
    return expected, k, s


@app.cell
def _(Solution, k, run_license_key_formatting, s):
    result = run_license_key_formatting(Solution, s, k)
    result
    return (result,)


@app.cell
def _(assert_license_key_formatting, expected, result):
    assert_license_key_formatting(result, expected)
    return


if __name__ == "__main__":
    app.run()
