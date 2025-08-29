.. _get_batch_results:

(GET) Get Batch Results
=======================

**Endpoint**

.. code-block:: bash

   GET /v2/api-integration/batch-results/{batch_id}

**Description**

Retrieves the results of a scheduled batch of tasks.

**Path Parameters**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Parameter
     - Description
   * - ``batch_id``
     - The unique identifier for the batch.

**Successful Response Example**

.. code-block:: json

   {
       "success": true,
       "message": "Batch results fetched successfully for batch ID: ef6c449f-75ec-4c34-bca0-d164895b5e47",
       "data": {
           "batch_id": "ef6c449f-75ec-4c34-bca0-d164895b5e47",
           "batch_status": "completed",
           "total_tasks": 2,
           "completed_tasks": 2,
           "scheduled_for": "2025-01-01T10:00:00Z",
           "executed_at": "2025-01-01T10:05:12Z",
           "tasks": [
               {
                   "task_id": "1267f677-a39a-4196-80aa-1be9a2b0a365",
                   "status": "PROCESS_COMPLETE",
                   "eligibility_result": {
                       "status": "failed",
                       "message": "Multiple beneficiaries found"
                   }
               },
               {
                   "task_id": "2378g788-b4bc-5287-91bb-2cf8b3c0b476",
                   "status": "PROCESS_COMPLETE",
                   "eligibility_result": {
                       "status": "found",
                       "data": {
                           "is_eligible": true,
                           "patient_info": {
                               "policy_holder_name": "[PATIENT_NAME]"
                           }
                       }
                   }
               }
           ]
       }
   }