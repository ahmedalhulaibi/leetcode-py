import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_crawl, run_crawl
    from solution import Solution

    return Solution, assert_crawl, run_crawl


@app.cell
def _():
    # Example test case
    urls = [
        "http://news.yahoo.com",
        "http://news.yahoo.com/news",
        "http://news.yahoo.com/news/topics/",
        "http://news.google.com",
        "http://news.yahoo.com/us",
    ]
    edges = [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]]
    start_url = "http://news.yahoo.com/news/topics/"
    expected = sorted(
        [
            "http://news.yahoo.com",
            "http://news.yahoo.com/news",
            "http://news.yahoo.com/news/topics/",
            "http://news.yahoo.com/us",
        ]
    )
    return edges, expected, start_url, urls


@app.cell
def _(Solution, edges, run_crawl, start_url, urls):
    result = run_crawl(Solution, urls, edges, start_url)
    result
    return (result,)


@app.cell
def _(assert_crawl, expected, result):
    assert_crawl(result, expected)
    return


if __name__ == "__main__":
    app.run()
