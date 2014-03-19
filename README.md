heroku
======
Sumitter 1 Name: Brian Whelan , Student Number: C10319509

Sumitter 2 Name: Andrew Tully , Student Number: C11347281

App url: http://immense-fjord-7601.herokuapp.com/

Testing Plans are below 

Test name: Create Calendar

	Goal: To create calendars with unique IDs
		
	Test Plan
		
	●	Calendar with an ID of 1 is created
		
	●	A second calendar with an ID of 1 is created
		
	●	A third calendar with an ID of 2 is created


	Test Results
	
	●	First Calendar is successfully created
	
	●	The second calendar is not created as the first calendar is already using the given ID
	
	●	The third calendar is created because it's ID is unused
	
	●	All responses are JSON encoded


Test name: View Calendar

	Goal:To view display all calendars, or display a specific calendar by providing an ID
	
	Test Plan
	
	●	Make two calendars with unique IDs
	
	●	Attempt to retrieve two calendars individually
	
	●	Attempt to retrieve nonexistent calendar
	
	●	Attempt to retrieve all existing calendars
	
	Test Results
	
	●	Calendars successfully created. JSON response is returned
	
	●	When retrieving a nonexistent calendar a JSON error is returned
	
	●	Calendars with valid IDs were retrieved individually. JSON encoded response was returned
	
	●	When all calendars are retrieved, the two ones which were created in the test are given. JSON encoded

Test name: Create Entry

	Goal:To add entries to multiple calendars, without causing cross-calendar conflict
	
	Test Plan
	
	●	Create two calendars with unique IDs
	
	●	Attempt to add an entry to a nonexistent calendar
	
	●	Add a unique entry with an ID of 1 to the first calendar
	
	●	Add a unique entry that also has an ID of 1 to the second calendar
	Results

	●	Two calendars successfully created. User notified by JSON encoded message
	
	●	When an entry was added to a nonexistent calendar a JSON encoded error message was returned
	
	●	TestEntry1 was successfully added to the first calendar. User notified by JSON encoded message

	●	TestEntry2 was successfully added to the second character, without causing an ID conflict (they have the same ID, but belong to different calendars). User notified by JSON encoded message

View Entry

	Goal: Display the contents of requested entries
	
	Test Plan
	
	●	Create two calendars with unique IDs
	
	●	Add a unique entry to each calendar
	
	●	Attempt to display a nonexistent entry
	
	●	Attempt to display actual entries upon request
	
	Test Results
	
	●	Two calendars successfully created. User notified by JSON encoded message
	
	●	Entries successfully added. User notified by JSON encoded message
	
	●	When a nonexistent entry was viewed a JSON encoded error message was returned
	
	●	TestEntry1 could be retrieved upon request (JSON encoded)
	
	●	TestEntry2 could be retrieved upon request (JSON encoded)

Modify Entry

	Goal:Change fields of an entry, and have them saved
	
	Test Plan
	
	●	Create a calendar
	
	●	Add a unique entry to the calendar
	
	●	Display all entries
	
	●	Attempt to change nonexistent entry
	
	●	Modify one entry in a calendar
	
	●	Display all entries
	
	Results
	
	●	Calendar was successfully created. User notified by JSON encoded message
	
	●	Entries successfully added. User notified by JSON encoded message
	
	●	When a nonexistent entry was modified a JSON encoded error message was returned
	
	●	All entries were successfully displayed
	
	●	Entry was successfully modified. User notified by JSON encoded message
	
	●	Entries were successfully displayed. The modified field was different to the original field

Delete Entry

	Goal:Permanently delete an entry from a field
	
	Test Plan
	
	●	Create a calendar
	
	●	Add a unique entry to a calendar
	
	●	Display all entries in calendar
	
	●	Attempt to delete nonexistent entry
	
	●	Delete an existing entry
	
	●	Display all entries
	
	Test Results
	
	●	Calendar was successfully created. User notified by JSON encoded message
	
	●	Entries successfully added. User notified by JSON encoded message
	
	●	When a nonexistent entry was deleted a JSON encoded error message was returned
	
	●	Entries successfully displayed.
	
	●	Entry successfully deleted. User notified by JSON encoded message
	
	●	Entries successfully displayed

Delete Calendar

	Goal:Delete a calendar, and ensure it’s entries are not linked to the ID
	
	Test Plan
	
	●	Create two calendars
	
	●	Add an entry to a calendar
	
	●	Display all calendars
	
	●	Delete the calendar containing an entry
	
	●	Display all calendars
	
	●	Create a new calendar with the same ID as the deleted calendar
	
	●	List all calendars
	
	Results
	
	●	Calendars was successfully created
	
	●	Entry is added to a calendar. User notified by JSON encoded message
	
	●	Calendars are successfully displayed
	
	●	Calendar successfully deleted. User notified by JSON encoded message
	
	●	Calendars are displayed. Deleted calendar is not displayed
	
	●	New calendar is created with the same ID as deleted calendar. User notified by JSON encoded message
	
	●	Calendars are listed. New calendar does not contain any data from the original calendar.
