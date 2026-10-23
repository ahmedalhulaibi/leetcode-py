import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sort_people, run_sort_people
    from solution import Solution

    return Solution, assert_sort_people, run_sort_people


@app.cell
def _():
    # Example test case
    names = ["Mary", "John", "Emma"]
    heights = [180, 165, 170]
    expected = ["Mary", "Emma", "John"]
    return expected, heights, names


@app.cell
def _(Solution, heights, names, run_sort_people):
    result = run_sort_people(Solution, names, heights)
    result
    return (result,)


@app.cell
def _(assert_sort_people, expected, result):
    assert_sort_people(result, expected)
    return


if __name__ == "__main__":
    app.run()
