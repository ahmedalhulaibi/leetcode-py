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
    # 2467. Most Profitable Path in a Tree

    **Medium** · Array, Tree, Depth-First Search, Breadth-First Search, Graph Theory

    There is an undirected tree with `n` nodes labeled from `0` to `n - 1`, rooted at node `0`. You are given a 2D integer array `edges` of length `n - 1` where `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]` indicates that there is an edge between nodes `a<sub>i</sub>` and `b<sub>i</sub>` in the tree.

    At every node `i`, there is a gate. You are also given an array of even integers `amount`, where `amount[i]` represents:

    - the price needed to open the gate at node `i`, if `amount[i]` is negative, or,
    - the cash reward obtained on opening the gate at node `i`, otherwise.

    The game goes on as follows:

    - Initially, Alice is at node `0` and Bob is at node `bob`.
    - At every second, Alice and Bob **each** move to an adjacent node. Alice moves towards some **leaf node**, while Bob moves towards node `0`.
    - For **every** node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
      - If the gate is **already open**, no price will be required, nor will there be any cash reward.
      - If Alice and Bob reach the node **simultaneously**, they share the price/reward for opening the gate there. In other words, if the price to open the gate is `c`, then both Alice and Bob pay `c / 2` each. Similarly, if the reward at the gate is `c`, both of them receive `c / 2` each.
    - If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node `0`, he stops moving. Note that these events are **independent** of each other.

    Return the **maximum** net income Alice can have if she travels towards the optimal leaf node.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/10/29/eg1.png)

    ```
    Input: edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
    Output: 6
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/10/29/eg2.png)

    ```
    Input: edges = [[0,1]], bob = 1, amount = [-7280,2350]
    Output: -7280
    ```

    ## Constraints

    - 2 <= n <= 10<sup>5</sup>
    - edges.length == n - 1
    - edges[i].length == 2
    - 0 <= a<sub>i</sub>, b<sub>i</sub> < n
    - a<sub>i</sub> != b<sub>i</sub>
    - edges represents a valid tree.
    - 1 <= bob < n
    - amount.length == n
    - amount[i] is an even integer in the range [-10<sup>4</sup>, 10<sup>4</sup>].



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def most_profitable_path(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
            raise NotImplementedError('Implement most_profitable_path')

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
