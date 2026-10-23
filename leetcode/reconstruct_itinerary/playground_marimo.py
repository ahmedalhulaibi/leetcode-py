import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_itinerary, run_find_itinerary
    from solution import Solution

    return Solution, assert_find_itinerary, run_find_itinerary


@app.cell
def _():
    # Example test case
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    expected = ["JFK", "MUC", "LHR", "SFO", "SJC"]
    return expected, tickets


@app.cell
def _(Solution, run_find_itinerary, tickets):
    result = run_find_itinerary(Solution, tickets)
    result
    return (result,)


@app.cell
def _(assert_find_itinerary, expected, result):
    assert_find_itinerary(result, expected)
    return


if __name__ == "__main__":
    app.run()
