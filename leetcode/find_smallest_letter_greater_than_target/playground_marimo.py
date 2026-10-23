import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_next_greatest_letter, run_next_greatest_letter
    from solution import Solution

    return Solution, assert_next_greatest_letter, run_next_greatest_letter


@app.cell
def _():
    # Example test case
    letters: list[str] = ["c", "f", "j"]
    target = "a"
    expected = "c"
    return expected, letters, target


@app.cell
def _(Solution, letters: list[str], run_next_greatest_letter, target):
    result = run_next_greatest_letter(Solution, letters, target)
    result
    return (result,)


@app.cell
def _(assert_next_greatest_letter, expected, result):
    assert_next_greatest_letter(result, expected)
    return


if __name__ == "__main__":
    app.run()
