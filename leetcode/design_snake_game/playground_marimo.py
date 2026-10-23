# /// script
# requires-python = ">=3.10"
# dependencies = ["marimo==0.25.2", "leetcode-py-sdk[practice]==0.0.0"]
# [tool.uv.sources]
# leetcode-py-sdk = { path = "../..", editable = true }
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from leetcode_py.practice import run_practice_tests

    return mo, run_practice_tests


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # 353. Design Snake Game

    **Medium** · Design, Queue, Array, Hash Table, Simulation

    Design a [Snake game](https://en.wikipedia.org/wiki/Snake_(video_game)) that is played on a device with screen size `height x width`.

    The snake is initially positioned at the top left corner `(0, 0)` with a length of `1` unit.

    You are given an array `food` where `food[i] = (r_i, c_i)` is the row and column position of a piece of food that the snake can eat. When a snake eats a piece of food, its length and the game's score both increase by `1`.

    Each piece of food appears one by one on the screen, meaning the second piece of food will not appear until the snake eats the first piece of food.

    When a piece of food appears on the screen, it is **guaranteed** that it will not appear on a block occupied by the snake.

    The game is over if the snake goes out of bounds (hits a wall) or if its head occupies a space that its body occupies **after** moving (i.e. a snake of length 4 cannot run into itself).

    Implement the `SnakeGame` class:

    - `SnakeGame(int width, int height, int[][] food)` Initializes the object with a screen of size `height x width` and the positions of the `food`.
    - `int move(String direction)` Returns the score of the game after applying one `direction` move by the snake. If the game is over, return `-1`.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0353.Design%20Snake%20Game/images/snake.jpg)

    ```
    Input
    ["SnakeGame", "move", "move", "move", "move", "move", "move"]
    [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
    Output
    [null, 0, 0, 1, 1, 2, -1]

    Explanation
    SnakeGame snakeGame = new SnakeGame(3, 2, [[1, 2], [0, 1]]);
    snakeGame.move("R"); // return 0
    snakeGame.move("D"); // return 0
    snakeGame.move("R"); // return 1, snake eats the first piece of food. The second piece of food appears at (0, 1).
    snakeGame.move("U"); // return 1
    snakeGame.move("L"); // return 2, snake eats the second food. No more food appears.
    snakeGame.move("U"); // return -1, game over because snake collides with border
    ```

    ## Constraints

    - `1 <= width, height <= 10^4`
    - `1 <= food.length <= 50`
    - `food[i].length == 2`
    - `0 <= r_i < height`
    - `0 <= c_i < width`
    - `direction.length == 1`
    - `direction` is `'U'`, `'D'`, `'L'`, or `'R'`.
    - At most `10^4` calls will be made to `move`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import deque

    class SnakeGame:

        def __init__(self, width: int, height: int, food: list[list[int]]) -> None:
            raise NotImplementedError('Implement __init__')

        def move(self, direction: str) -> int:
            raise NotImplementedError('Implement move')

    practice_exports = {'deque': deque, 'SnakeGame': SnakeGame}
    return (practice_exports,)


@app.cell(hide_code=True)
def _(mo):
    run_tests = mo.ui.run_button(label="Run tests")
    run_tests
    return (run_tests,)


@app.cell(hide_code=True)
def _(mo, practice_exports, run_practice_tests, run_tests):
    mo.stop(not run_tests.value, mo.md("Implement your solution, then run the tests."))
    test_result = run_practice_tests(mo.notebook_dir(), practice_exports)
    mo.vstack([
        mo.md(f"**{test_result.passed} passed · {test_result.failed} failed · "
              f"{test_result.skipped} skipped**"),
        mo.md("**All tests passed.**" if test_result.exit_code == 0 else "**Tests are not passing yet.**"),
        mo.accordion({"Test output": mo.plain_text(test_result.output)}),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Notes

    Record your approach, complexity, and edge cases here.
    """)
    return


if __name__ == "__main__":
    app.run()
