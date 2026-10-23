import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_predict_party_victory, run_predict_party_victory
    from solution import Solution

    return Solution, assert_predict_party_victory, run_predict_party_victory


@app.cell
def _():
    # Example test case
    senate = "RD"
    expected = "Radiant"
    return expected, senate


@app.cell
def _(Solution, run_predict_party_victory, senate):
    result = run_predict_party_victory(Solution, senate)
    result
    return (result,)


@app.cell
def _(assert_predict_party_victory, expected, result):
    assert_predict_party_victory(result, expected)
    return


if __name__ == "__main__":
    app.run()
