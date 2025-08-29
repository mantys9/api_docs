.. _create_bulk_tasks:

(POST) Create Bulk Eligibility Tasks
====================================

**Endpoint**

.. code-block:: bash

   POST /v2/api-integration/bulk/create-tasks

**Description**

Creates multiple eligibility verification tasks in a single request. This is more efficient than sending multiple individual requests.

**Request Body**

The request body should contain a ``requests`` array, where each object is a single task creation payload.

.. code-block:: json

   {
       "requests": [
           {
               "id_value": "784-XXXX-XXXXXXX-X",
               "id_type": "EMIRATESID",
               "tpa_name": "TPA002",
               "visit_type": "OUTPATIENT",
               "extra_args": {
                   "title": "",
                   "value": ""
               },
               "doctorName": "",
               "payerName": ""
           },
           {
               "id_value": "784-YYYY-YYYYYYY-Y",
               "id_type": "EMIRATESID",
               "tpa_name": "TPA002",
               "visit_type": "OUTPATIENT",
               "extra_args": {
                   "title": "",
                   "value": ""
               },
               "doctorName": "",
               "payerName": ""
           }
       ]
   }

**Successful Response Example**

.. code-block:: json

   {
       "success": true,
       "message": "Bulk tasks created successfully. 2 tasks created.",
       "data": {
           "tasks": [
               {
                   "task_id": "c5d5093f-8c49-4b6b-a83e-f90b6af7dee8",
                   "status": "pending",
                   "patient_info": {
                       "name": null,
                       "id_value": "784-XXXX-XXXXXXX-X",
                       "tpa_name": "TPA002"
                   },
                   "is_search_all": false
               },
               {
                   "task_id": "d6e61a4g-9d5a-5c7c-b94f-g01c7bg8eff9",
                   "status": "pending",
                   "patient_info": {
                       "name": null,
                       "id_value": "784-YYYY-YYYYYYY-Y",
                       "tpa_name": "TPA002"
                   },
                   "is_search_all": false
               }
           ],
           "total_created": 2
       }
   }

**Successful Response Example (Search All)**

.. code-block:: json

   {
       "success": true,
       "message": "Bulk tasks created successfully. 1 tasks created.",
       "data": {
           "tasks": [
               {
                   "task_id": "c5d5093f-8c49-4b6b-a83e-f90b6af7dee8",
                   "status": "pending",
                   "patient_info": {
                       "name": null,
                       "id_value": "784-XXXX-XXXXXXX-X",
                       "tpa_name": "TPA002"
                   },
                   "is_search_all": false
               }
           ],
           "total_created": 1
       }
   }