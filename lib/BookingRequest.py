class BookingRequest: 

    def __init__(self, start_date, end_date, property_id, user_id, booking_id, booking_status, property_name=None, property_description=None, property_location=None):
        self.start_date = start_date
        self.end_date = end_date
        self.status = booking_status
        self.property_id = property_id
        self.user_id = user_id
        self.booking_id = booking_id
        
        # Extra fields for the read-only booking detail page.
        self.property_name = property_name
        self.property_description = property_description
        self.property_location = property_location

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def rejectRequest(self): 
        # Call this method if the owner doesn't want to accept this request.
        self.status = 'REJECTED'
        #return True

    def approveRequest(self): 
        # Call this method if the owner wishes accept this request.
        self.status = 'APPROVED'
        #return True