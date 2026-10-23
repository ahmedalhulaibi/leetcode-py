import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_check_inclusion, run_check_inclusion
    from solution import Solution

    return Solution, assert_check_inclusion, run_check_inclusion


@app.cell
def _():
    # Example test case
    s1 = "ab"
    s2 = "eidbaooo"
    expected = True
    return expected, s1, s2


@app.cell
def _(Solution, run_check_inclusion, s1, s2):
    result = run_check_inclusion(Solution, s1, s2)
    result
    return (result,)


@app.cell
def _(assert_check_inclusion, expected, result):
    assert_check_inclusion(result, expected)
    return


if __name__ == "__main__":
    app.run()
