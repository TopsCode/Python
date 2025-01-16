"""
Endpoint: POST /students/create/
Body (JSON):

{
  "first_name": "priya",
  "last_name": "patel",
  "age": 20,
  "email": "priya.patel@example.com"
}

Get all students:

Endpoint: GET /students/

Get a specific student by ID:
Endpoint: GET /students/<student_id>/


Update a student:
Endpoint: PUT /students/update/<student_id>/
Body (JSON):
{
  "first_name": "priya",
  "last_name": "patel",
  "age": 21,
  "email": "priya.patel@newdomain.com"
}

Delete a student:
Endpoint: DELETE /students/delete/<student_id>/
"""