import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_score_sightseeing_pair, run_max_score_sightseeing_pair
    from solution import Solution

    return (
        Solution,
        assert_max_score_sightseeing_pair,
        run_max_score_sightseeing_pair,
    )


@app.cell
def _():
    # Example test case
    values = [8, 1, 5, 2, 6]
    expected = 11
    return expected, values


@app.cell
def _(Solution, run_max_score_sightseeing_pair, values):
    result = run_max_score_sightseeing_pair(Solution, values)
    result
    return (result,)


@app.cell
def _(assert_max_score_sightseeing_pair, expected, result):
    assert_max_score_sightseeing_pair(result, expected)
    return


if __name__ == "__main__":
    app.run()
