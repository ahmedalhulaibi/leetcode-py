import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_asteroid_collision, run_asteroid_collision
    from solution import Solution

    return Solution, assert_asteroid_collision, run_asteroid_collision


@app.cell
def _():
    # Example test case
    asteroids = [5, 10, -5]
    expected = [5, 10]
    return asteroids, expected


@app.cell
def _(Solution, asteroids, run_asteroid_collision):
    result = run_asteroid_collision(Solution, asteroids)
    result
    return (result,)


@app.cell
def _(assert_asteroid_collision, expected, result):
    assert_asteroid_collision(result, expected)
    return


if __name__ == "__main__":
    app.run()
