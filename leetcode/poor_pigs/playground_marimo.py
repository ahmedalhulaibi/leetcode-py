import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_poor_pigs, run_poor_pigs
    from solution import Solution

    return Solution, assert_poor_pigs, run_poor_pigs


@app.cell
def _():
    # Example test case
    buckets: int = 4
    minutes_to_die: int = 15
    minutes_to_test: int = 15
    expected: int = 2
    return buckets, expected, minutes_to_die, minutes_to_test


@app.cell
def _(
    Solution,
    buckets: int,
    minutes_to_die: int,
    minutes_to_test: int,
    run_poor_pigs,
):
    result = run_poor_pigs(Solution, buckets, minutes_to_die, minutes_to_test)
    result
    return (result,)


@app.cell
def _(assert_poor_pigs, expected: int, result):
    assert_poor_pigs(result, expected)
    return


if __name__ == "__main__":
    app.run()
