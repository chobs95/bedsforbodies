# Users should be able to offer a range of dates where their space is available.
    ## End user to use a simple calendar picker to enter a start and end date for each 'space'
    ## (Nice to have) - validation of non overlapping dates

    ### Class
    ### Properties
    name
    start date, end date {collection}
    Price_per_night(unit to be defined)

    ### methods
    addAvailability(startDate, endDate)
    removeAvailability(startDate, endDate)
    setCost(defined_cost)
    intilisation(name) # include setCost
    displayAvailability() # This will let the GUI know which dates are 'pickable'. This will prevent the end user from picking an existing 'booked' date. Maybe share by calendar month?


    Data and/or Repository - maybe use ORM instead.


# Unit Tests 
- Test object creation
- Number validation - Nice to have.
- Add/remove availability

# Integration tests










