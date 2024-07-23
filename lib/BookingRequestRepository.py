from lib.BookingRequest import BookingRequest

from datetime import datetime

class BookingRequestRepository():

    def __init__(self, connection):
        self._connection = connection

    def all(self):

        rows = self._connection.execute('SELECT property_id, user_id, start_date, end_date, id, status from bookings') 
        booking_requests = []
        for row in rows:

            end_date_obj = row["end_date"]
            start_date_obj = row["start_date"]

            br =  BookingRequest(start_date_obj, end_date_obj, row["property_id"], row["user_id"], row["id"], row["status"])
            
            booking_requests.append(br)

        return booking_requests
    
    def get_request_detail(self, booking_id):

        rows = self._connection.execute('SELECT bookings.property_id, bookings.user_id, bookings.status, bookings.start_date, bookings.end_date, bookings.id, properties.property, properties. description, properties.location from bookings inner join properties ON bookings.property_id = properties.id WHERE bookings.id= %s', [booking_id]) 
        # There should be only 1 row. 
        row = rows[0]

        # property_name=None, property_description=None, property_location=None
        end_date_obj = row["end_date"]
        start_date_obj = row["start_date"]
        br =  BookingRequest(start_date_obj, end_date_obj, row["property_id"], row["user_id"], row["id"], row["status"], row["property"], row["description"], row["location"])
        return br
    
    def create(self, BookingRequest):
        rows = self._connection.execute(
            'INSERT INTO bookings (property_id, user_id, start_date, end_date, status) VALUES (%s, %s, %s, %s, %s)', 
            [BookingRequest.property_id, BookingRequest.user_id, BookingRequest.start_date, BookingRequest.end_date, BookingRequest.status])
        return None
    
    def update_booking_rejected(self, booking_id):
        # print('=> here is the status and id fields: ', BookingRequest.status, ' : ' , BookingRequest.booking_id)
        rows = self._connection.execute("UPDATE bookings SET status='REJECTED' WHERE id = %s", [booking_id])
        return None

    def update_booking_approved(self, booking_id):
        #print('=> here is the status and id fields: ', BookingRequest.status, ' : ' , BookingRequest.booking_id)
        rows = self._connection.execute("UPDATE bookings SET status='APPROVED' WHERE id = %s", [booking_id])
        return None

    # # Delete a BookingReference.
    # def delete(self, booking_request_id):
    #     self._connection.execute(
    #         'DELETE FROM bookings WHERE id = %s', [booking_request_id])
    #     return None

    # Find bookingReferences by the user/customer.
    def get_bookings_by_customer(self, user_id):
        
        booking_requests= []
        rows = self._connection.execute('SELECT * FROM bookings WHERE user_id = %s', [user_id])
        
        for row in rows:
            br =  BookingRequest(row["start_date"], row["end_date"], row["property_id"], row["user_id"], row["id"], row["status"])            
            booking_requests.append(br)

        return booking_requests
    
    # # Find bookingReferences by their property.
    # def get_bookings_by_property(self, property_id):
        
    #     booking_requests= []

    #     rows = self._connection.execute(
    #         'SELECT * from bookings WHERE property_id = %s', [property_id])
        
    #     for row in rows:

    #         end_date_obj = row["end_date"]
    #         start_date_obj = row["start_date"]

    #         br =  BookingRequest(start_date_obj, end_date_obj, row["property_id"], row["user_id"], row["id"], row["status"])            

    #         booking_requests.append(br)

    #     return booking_requests