import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_all_people, run_find_all_people
    from solution import Solution

    return Solution, assert_find_all_people, run_find_all_people


@app.cell
def _():
    # Example test case
    n = 6
    meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]]
    first_person = 1
    expected = [0, 1, 2, 3, 5]
    return expected, first_person, meetings, n


@app.cell
def _(Solution, first_person, meetings, n, run_find_all_people):
    result = run_find_all_people(Solution, n, meetings, first_person)
    result
    return (result,)


@app.cell
def _(assert_find_all_people, expected, result):
    assert_find_all_people(result, expected)
    return


if __name__ == "__main__":
    app.run()
