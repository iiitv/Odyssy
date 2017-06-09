# API for announcement app

It uses the djangorestframework and the url is `(BASE_URL/api/announcement)`. It will show the browsable api view.
To Fetch the result in the form of json, The query url has to be modified as `(BASE_URL/api/announcement?format=json)`

## API Details

`BASEURL + api/announcement/` - returns all the announcement
`BASEURL + api/announcement/<key>` - returns the detail of announcement matching that key
`BASEURL + api/announcement/tag/<tag_name>` - returns all the announcements with the tag_name
`BASEURL + api/announcement/latest/<count>` - returns the latest announcements (size `=` count)

## NOTE

If there is no match them the api will send an empty json response.
