import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_judge_point24, run_judge_point24
    from solution import Solution

    return Solution, assert_judge_point24, run_judge_point24


@app.cell
def _():
    # Example test case
    cards = [4, 1, 8, 7]
    expected = True
    return cards, expected


@app.cell
def _(Solution, cards, run_judge_point24):
    result = run_judge_point24(Solution, cards)
    result
    return (result,)


@app.cell
def _(assert_judge_point24, expected, result):
    assert_judge_point24(result, expected)
    return


if __name__ == "__main__":
    app.run()
