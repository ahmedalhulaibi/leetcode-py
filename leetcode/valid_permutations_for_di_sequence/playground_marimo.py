import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_perms_di_sequence, run_num_perms_di_sequence
    from solution import Solution

    return Solution, assert_num_perms_di_sequence, run_num_perms_di_sequence


@app.cell
def _():
    # Example test case
    s = "DID"
    expected = 5
    return expected, s


@app.cell
def _(Solution, run_num_perms_di_sequence, s):
    result = run_num_perms_di_sequence(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_num_perms_di_sequence, expected, result):
    assert_num_perms_di_sequence(result, expected)
    return


if __name__ == "__main__":
    app.run()
