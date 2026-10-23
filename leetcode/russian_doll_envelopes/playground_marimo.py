import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_envelopes, run_max_envelopes
    from solution import Solution

    return Solution, assert_max_envelopes, run_max_envelopes


@app.cell
def _():
    # Example test case
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    expected = 3
    return envelopes, expected


@app.cell
def _(Solution, envelopes, run_max_envelopes):
    result = run_max_envelopes(Solution, envelopes)
    result
    return (result,)


@app.cell
def _(assert_max_envelopes, expected, result):
    assert_max_envelopes(result, expected)
    return


if __name__ == "__main__":
    app.run()
