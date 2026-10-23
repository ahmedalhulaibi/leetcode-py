import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_number_of_alternating_groups, run_number_of_alternating_groups
    from solution import Solution

    return (
        Solution,
        assert_number_of_alternating_groups,
        run_number_of_alternating_groups,
    )


@app.cell
def _():
    # Example test case
    colors = [0, 1, 0, 1, 0]
    k = 3
    expected = 3
    return colors, expected, k


@app.cell
def _(Solution, colors, k, run_number_of_alternating_groups):
    result = run_number_of_alternating_groups(Solution, colors, k)
    result
    return (result,)


@app.cell
def _(assert_number_of_alternating_groups, expected, result):
    assert_number_of_alternating_groups(result, expected)
    return


if __name__ == "__main__":
    app.run()
