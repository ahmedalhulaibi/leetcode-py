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
    # 1564. Put Boxes Into the Warehouse I

    **Medium** · Greedy, Array, Sorting

    You are given two arrays of positive integers, `boxes` and `warehouse`, representing the heights of some boxes of unit width and the heights of `n` rooms in a warehouse respectively. The warehouse's rooms are labelled from `0` to `n - 1` from left to right where `warehouse[i]` (0-indexed) is the height of the i<sup>th</sup> room.

    Boxes are put into the warehouse by the following rules:

    - Boxes cannot be stacked.
    - You can rearrange the insertion order of the boxes.
    - Boxes can only be pushed into the warehouse from left to right only.
    - If the height of some room in the warehouse is less than the height of a box, then that box and all other boxes behind it will be stopped before that room.

    Return <em>the maximum number of boxes you can put into the warehouse.</em>

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1564.Put%20Boxes%20Into%20the%20Warehouse%20I/images/11.png)

    ```
    Input: boxes = [4,3,4,1], warehouse = [5,3,3,4,1]
    Output: 3
    Explanation:
    ![Explanation 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1564.Put%20Boxes%20Into%20the%20Warehouse%20I/images/12.png)
    We can first put the box of height 1 in room 4. Then we can put the box of height 3 in either of the 3 rooms 1, 2, or 3. Lastly, we can put one box of height 4 in room 0.
    There is no way we can fit all 4 boxes in the warehouse.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1564.Put%20Boxes%20Into%20the%20Warehouse%20I/images/21.png)

    ```
    Input: boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
    Output: 3
    Explanation:
    ![Explanation 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1564.Put%20Boxes%20Into%20the%20Warehouse%20I/images/22.png)
    Notice that it's not possible to put the box of height 4 into the warehouse since it cannot pass the first room of height 3.
    Also, for the last two rooms, 2 and 3, only boxes of height 1 can fit.
    We can fit 3 boxes maximum as shown above. The yellow box can also be put in room 2 instead.
    Swapping the orange and green boxes is also valid, or swapping one of them with the red box.
    ```

    ```
    Input: boxes = [1,2,3], warehouse = [1,2,3,4]
    Output: 1
    Explanation: Since the first room in the warehouse is of height 1, we can only put boxes of height 1.
    ```

    ## Constraints

    - `n == warehouse.length`
    - `1 <= boxes.length, warehouse.length <= 10^5`
    - `1 <= boxes[i], warehouse[i] <= 10^9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_boxes_in_warehouse(self, boxes: list[int], warehouse: list[int]) -> int:
            raise NotImplementedError('Implement max_boxes_in_warehouse')

    practice_exports = {'Solution': Solution}
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
