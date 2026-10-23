import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_strong_password_checker, run_strong_password_checker
    from solution import Solution

    return (
        Solution,
        assert_strong_password_checker,
        run_strong_password_checker,
    )


@app.cell
def _():
    # Example test case
    password = "a"
    expected = 5
    return expected, password


@app.cell
def _(Solution, password, run_strong_password_checker):
    result = run_strong_password_checker(Solution, password)
    result
    return (result,)


@app.cell
def _(assert_strong_password_checker, expected, result):
    assert_strong_password_checker(result, expected)
    return


if __name__ == "__main__":
    app.run()
