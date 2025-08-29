.. _get_last_5_tasks:

(GET) Get Last 5 Tasks
======================

**Endpoint**

.. code-block:: bash

   GET /v2/api-integration/last-5-tasks

**Description**

Retrieves the five most recent eligibility tasks for the clinic.

**Successful Response Example**

.. code-block:: json

   [
       {
           "id": "8af08f11-a437-49e2-92da-0e1ddff38f7d",
           "task_id": "5895a23d-df5c-4af4-b5b1-f9d2c944ac83",
           "status": "PROCESS_COMPLETE",
           "created_at": "2025-06-05T21:16:21.958547",
           "updated_at": "2025-06-05T21:17:28.510633",
           "request_dump": {
               "id_type": "EMIRATESID",
               "id_value": "784-XXXX-XXXXXXX-X",
               "tpa_name": "TPA002",
               "visit_type": "OUTPATIENT"
           },
           "eligibility_result": {
               "data_dump": {
                   "tpa": "TPA002",
                   "data": {
                       "is_eligible": true,
                       "patient_info": {
                           "patient_emirates_id": "784-XXXX-XXXXXXX-X",
                           "policy_holder_name": "[PATIENT_NAME]"
                       }
                   }
               }
           }
       }
   ]