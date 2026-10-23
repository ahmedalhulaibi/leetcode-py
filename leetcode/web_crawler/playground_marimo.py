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
    # 1236. Web Crawler

    **Medium** · Depth-First Search, Breadth-First Search, String, Interactive

    Given a url `startUrl` and an interface `HtmlParser`, implement a web crawler to crawl all links that are under the same hostname as `startUrl`.

    Return all urls obtained by your web crawler in **any** order.

    Your crawler should:

    - Start from the page: `startUrl`
    - Call `HtmlParser.getUrls(url)` to get all urls from a webpage of given url.
    - Do not crawl the same link twice.
    - Explore only the links that are under the same hostname as `startUrl`.

    ![Hostname](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1236.Web%20Crawler/images/urlhostname.png)

    As shown in the example url above, the hostname is `example.org`. For simplicity sake, you may assume all urls use http protocol without any port specified. For example, the urls `http://leetcode.com/problems` and `http://leetcode.com/contest` are under the same hostname, while urls `http://example.org/test` and `http://example.com/abc` are not under the same hostname.

    The `HtmlParser` interface is defined as such:

    ```
    interface HtmlParser {
      // Return a list of all urls from a webpage of given url.
      public List<String> getUrls(String url);
    }
    ```

    Below are two examples explaining the functionality of the problem, for custom testing purposes you'll have three variables `urls`, `edges` and `startUrl`. Notice that you will only have access to `startUrl` in your code, while `urls` and `edges` are not directly accessible to you in code.

    Note: Consider the same URL with the trailing slash `/` as a different URL. For example, `http://news.yahoo.com`, and `http://news.yahoo.com/` are different urls.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1236.Web%20Crawler/images/sample_2_1497.png)

    ```
    Input:
    urls = [
      "http://news.yahoo.com",
      "http://news.yahoo.com/news",
      "http://news.yahoo.com/news/topics/",
      "http://news.google.com",
      "http://news.yahoo.com/us"
    ]
    edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
    startUrl = "http://news.yahoo.com/news/topics/"
    Output:
    [
      "http://news.yahoo.com",
      "http://news.yahoo.com/news",
      "http://news.yahoo.com/news/topics/",
      "http://news.yahoo.com/us"
    ]
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1236.Web%20Crawler/images/sample_3_1497.png)

    ```
    Input:
    urls = [
      "http://news.yahoo.com",
      "http://news.yahoo.com/news",
      "http://news.yahoo.com/news/topics/",
      "http://news.google.com"
    ]
    edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
    startUrl = "http://news.google.com"
    Output: ["http://news.google.com"]
    Explanation: The startUrl links to all other pages that do not share the same hostname.
    ```

    ## Constraints

    - `1 <= urls.length <= 1000`
    - `1 <= urls[i].length <= 300`
    - `startUrl` is one of the `urls`.
    - Hostname label must be from 1 to 63 characters long, including the dots, may contain only the ASCII letters from 'a' to 'z', digits from '0' to '9' and the hyphen-minus character ('-').
    - The hostname may not start or end with the hyphen-minus character ('-').
    - You may assume there're no duplicates in url library.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class HtmlParser:

        def __init__(self, urls: list[str], edges: list[list[int]]) -> None:
            self.adj: dict[str, list[str]] = {u: [] for u in urls}
            for a, b in edges:
                self.adj[urls[a]].append(urls[b])

        def get_urls(self, url: str) -> list[str]:
            return self.adj[url]

    class Solution:

        def crawl(self, start_url: str, html_parser: HtmlParser) -> list[str]:
            raise NotImplementedError('Implement crawl')

    practice_exports = {'HtmlParser': HtmlParser, 'Solution': Solution}
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
