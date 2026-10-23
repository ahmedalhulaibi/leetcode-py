import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_survived_robots_healths, run_survived_robots_healths
    from solution import Solution

    return (
        Solution,
        assert_survived_robots_healths,
        run_survived_robots_healths,
    )


@app.cell
def _():
    # Example test case
    positions = [3, 5, 2, 6]
    healths = [10, 10, 15, 12]
    directions = "RLRL"
    expected = [14]
    return directions, expected, healths, positions


@app.cell
def _(Solution, directions, healths, positions, run_survived_robots_healths):
    result = run_survived_robots_healths(Solution, positions, healths, directions)
    result
    return (result,)


@app.cell
def _(assert_survived_robots_healths, expected, result):
    assert_survived_robots_healths(result, expected)
    return


if __name__ == "__main__":
    app.run()
