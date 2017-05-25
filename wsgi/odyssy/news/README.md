# News

Contains following views
* /news/ : Paginated list, with 3 items per page.
* /news/\<id> : Single item view.

3 latest news are displayed at index page. You can configure it using
environment variable NUM_EVENTS_ON_INDEX_PAGE. Default value is 3.

Use administrator panel to manage events.

Output is displayed in format \<News id> : <News Title>
