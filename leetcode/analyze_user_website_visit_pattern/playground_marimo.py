import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_most_visited_pattern, run_most_visited_pattern
    from solution import Solution

    return Solution, assert_most_visited_pattern, run_most_visited_pattern


@app.cell
def _():
    # Example test case
    username = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"]
    timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    website = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
    expected = ["home", "about", "career"]
    return expected, timestamp, username, website


@app.cell
def _(Solution, run_most_visited_pattern, timestamp, username, website):
    result = run_most_visited_pattern(Solution, username, timestamp, website)
    result
    return (result,)


@app.cell
def _(assert_most_visited_pattern, expected, result):
    assert_most_visited_pattern(result, expected)
    return


if __name__ == "__main__":
    app.run()
