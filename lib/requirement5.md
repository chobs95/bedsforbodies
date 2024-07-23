# Any signed-up user can request to hire any space for one night, and this should be approved by the user that owns that space.
## Register end user
## Authenticate end user
### Implement a flask session for this successful login.
## Authenticated end user has the ability to lodge a 'request' which must be reviewed by the 'space owner'
### Each request needs a status e.g. Pending, Rejected, Approved.

# class PropertyRequest
## properties
*databaseID*
start_date
end_date
status : rejected, approved, pending
property_id
customer_id
~~property_owner_id~~

## methods
reject
approve // check that the dates are availble before a commit.
constructor(startDate, endDate, customer_id, property_id)


Confirm that the customer and owner classes are defined **Can decide on 1 or 2 classes later on. ORM vs Repository classes **
