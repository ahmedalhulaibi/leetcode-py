import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_long_pressed_name, run_is_long_pressed_name
    from solution import Solution

    return Solution, assert_is_long_pressed_name, run_is_long_pressed_name


@app.cell
def _():
    # Example test case
    name = "alex"
    typed = "aaleex"
    expected = True
    return expected, name, typed


@app.cell
def _(Solution, name, run_is_long_pressed_name, typed):
    result = run_is_long_pressed_name(Solution, name, typed)
    result
    return (result,)


@app.cell
def _(assert_is_long_pressed_name, expected, result):
    assert_is_long_pressed_name(result, expected)
    return


if __name__ == "__main__":
    app.run()
