import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_seniors, run_count_seniors
    from solution import Solution

    return Solution, assert_count_seniors, run_count_seniors


@app.cell
def _():
    # Example test case
    details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
    expected = 2
    return details, expected


@app.cell
def _(Solution, details, run_count_seniors):
    result = run_count_seniors(Solution, details)
    result
    return (result,)


@app.cell
def _(assert_count_seniors, expected, result):
    assert_count_seniors(result, expected)
    return


if __name__ == "__main__":
    app.run()
