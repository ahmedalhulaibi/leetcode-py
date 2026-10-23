import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_music_playlists, run_num_music_playlists
    from solution import Solution

    return Solution, assert_num_music_playlists, run_num_music_playlists


@app.cell
def _():
    # Example test case
    n = 3
    goal = 3
    k = 1
    expected = 6
    return expected, goal, k, n


@app.cell
def _(Solution, goal, k, n, run_num_music_playlists):
    result = run_num_music_playlists(Solution, n, goal, k)
    result
    return (result,)


@app.cell
def _(assert_num_music_playlists, expected, result):
    assert_num_music_playlists(result, expected)
    return


if __name__ == "__main__":
    app.run()
