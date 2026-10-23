import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_repeat_limited_string, run_repeat_limited_string
    from solution import Solution

    return Solution, assert_repeat_limited_string, run_repeat_limited_string


@app.cell
def _():
    # Example test case
    s = "cczazcc"
    repeat_limit = 3
    expected = "zzcccac"
    return expected, repeat_limit, s


@app.cell
def _(Solution, repeat_limit, run_repeat_limited_string, s):
    result = run_repeat_limited_string(Solution, s, repeat_limit)
    result
    return (result,)


@app.cell
def _(assert_repeat_limited_string, expected, result):
    assert_repeat_limited_string(result, expected)
    return


if __name__ == "__main__":
    app.run()
