# Events

Contains following views
* /events/ : Paginated list, with 3 items per page.
* /events/<id> : Single item view.

3 latest events are displayed at index page. You can configure it using
environment variable NUM_EVENTS_ON_INDEX_PAGE. Default value is 3.

Use administrator panel to manage events.

Output is displayed in format \<Event Description> at \<Event Place> on \<Date>
