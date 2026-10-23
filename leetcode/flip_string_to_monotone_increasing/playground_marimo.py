import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_flips_mono_increasing, run_min_flips_mono_increasing
    from solution import Solution

    return (
        Solution,
        assert_min_flips_mono_increasing,
        run_min_flips_mono_increasing,
    )


@app.cell
def _():
    # Example test case
    s = "00110"
    expected = 1
    return expected, s


@app.cell
def _(Solution, run_min_flips_mono_increasing, s):
    result = run_min_flips_mono_increasing(Solution, s)
    result
    return (result,)


@app.cell
def _(assert_min_flips_mono_increasing, expected, result):
    assert_min_flips_mono_increasing(result, expected)
    return


if __name__ == "__main__":
    app.run()
