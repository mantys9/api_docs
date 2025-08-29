.. _schedule_batch_tasks:

(POST) Schedule Batch Tasks
===========================

**Endpoint**

.. code-block:: bash

   POST /v2/api-integration/schedule-tasks

**Description**

Schedules a batch of eligibility checks to be run at a later time.

**Request Body**

The request body should contain a ``requests`` array with task details and optional scheduling parameters.

**Additional Fields for Scheduling:**

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``phone``
     - String
     - Optional. Patient's phone number.
   * - ``name``
     - String
     - Optional. Patient's name.
   * - ``dob``
     - String
     - Optional. Patient's date of birth (YYYY-MM-DD format).
   * - ``mode``
     - String
     - Optional. Processing mode (e.g., "prod").
   * - ``test_mode``
     - Boolean
     - Optional. Whether this is a test request.
   * - ``scheduled_for``
     - String
     - Optional. ISO 8601 timestamp for when to run the batch.

**Request Example**

.. code-block:: json

   {
       "requests": [
           {
               "tpa_name": "TPA002",
               "id_value": "784-XXXX-XXXXXXX-X",
               "id_type": "EMIRATESID",
               "phone": "0501234567",
               "name": "[PATIENT_NAME]",
               "dob": "YYYY-MM-DD",
               "visit_type": "OUTPATIENT",
               "doctorName": "Dr. Smith",
               "mode": "prod",
               "test_mode": false,
               "extra_args": {
                   "note": "example 1"
               }
           },
           {
               "tpa_name": "DHPO",
               "id_value": "784-YYYY-YYYYYYY-Y",
               "id_type": "EMIRATESID",
               "name": "[PATIENT_NAME]",
               "visit_type": "OUTPATIENT",
               "mode": "prod",
               "test_mode": false
           }
       ],
       "scheduled_for": "2025-01-01T10:00:00Z",
       "description": "Morning batch for clinic A"
   }

**Successful Response Example**

.. code-block:: json

   {
       "success": true,
       "message": "Tasks scheduled successfully. 2 tasks scheduled with batch ID: 181ea081-56f2-403b-9e20-cc7d461ff479. Results expected by 2025-08-18T06:00:00+04:00.",
       "data": {
           "batch_id": "181ea081-56f2-403b-9e20-cc7d461ff479",
           "total_scheduled": 2
       }
   }