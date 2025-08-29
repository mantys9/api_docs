.. _get_bulk_results:

(POST) Get Bulk Eligibility Task Results
========================================

**Endpoint**

.. code-block:: bash

   POST /v2/api-integration/bulk/get-results

**Description**

Retrieves the results for multiple eligibility tasks at once by providing a list of ``task_ids``.

**Request Body**

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``task_ids``
     - Array of Strings
     - **Required.** A list of unique task identifiers to retrieve results for.

**Request Example**

.. code-block:: json

   {
       "task_ids": ["a8ba9656-017a-4a06-bc13-916a6514d9a8", "feece3c1-d222-4051-87cc-fc2bc2b6e191"]
   }

**Successful Response Example**

The response contains a ``results`` array, where each object corresponds to a requested task. The ``status`` of each task can be ``PROCESS_COMPLETE``, ``failed``, or an in-progress status such as ``NAVIGATING_WEBSITE`` or ``EXTRACTING_DATA``.

.. code-block:: json

   {
       "success": true,
       "message": "Bulk results fetched successfully.",
       "data": {
           "results": [
               {
                   "task_id": "a8ba9656-017a-4a06-bc13-916a6514d9a8",
                   "status": "PROCESS_COMPLETE",
                   "is_search_all": false,
                   "created_at": "2025-08-03T07:57:10.488613",
                   "updated_at": "2025-08-03T07:58:32.197441",
                   "eligibility_result": {
                       "status": "found",
                       "data": {
                           "is_eligible": true,
                           "patient_info": {
                               "policy_holder_name": "[PATIENT_NAME]",
                               "patient_emirates_id": "784-XXXX-XXXXXXX-X"
                           }
                       }
                   }
               },
               {
                   "task_id": "feece3c1-d222-4051-87cc-fc2bc2b6e191",
                   "status": "PROCESS_COMPLETE",
                   "is_search_all": false,
                   "created_at": "2025-08-03T08:01:15.123456",
                   "updated_at": "2025-08-03T08:02:45.654321",
                   "eligibility_result": {
                       "data_dump": {
                           "status": "member_not_found",
                           "message": "`This beneficiary is Invalid` was seen",
                           "error_type": "MemberNotFoundError"
                       }
                   }
               },
               {
                   "task_id": "851bda78-4a2d-4827-ab5f-cd4245bd6ffa",
                   "status": "NAVIGATING_WEBSITE",
                   "is_search_all": false,
                   "created_at": "2025-08-03T09:10:00.000000",
                   "updated_at": "2025-08-03T09:10:05.123456",
                   "eligibility_result": null
               },
               {
                   "task_id": "9bfd8a6e-5b3c-4f8e-9b3a-5e6f7a8d9c0b",
                   "status": "EXTRACTING_DATA",
                   "is_search_all": false,
                   "created_at": "2025-08-03T09:12:00.000000",
                   "updated_at": "2025-08-03T09:12:30.987654",
                   "interim_results": {
                       "tpa_name": "TPA002",
                       "screenshot_key": "https://s3.me-central-1.amazonaws.com/..."
                   },
                   "eligibility_result": null
               }
           ]
       }
   }

**Successful Response Example (Search All)**

The response for a bulk request that includes multi-provider search tasks (`"tpa_name": "BOTH"`) will contain tasks with ``"is_search_all": true``. The structure for these results includes an ``aggregated_results`` array for completed tasks.

.. code-block:: json

   {
       "success": true,
       "message": "Bulk results fetched successfully.",
       "data": {
           "results": [
               {
                   "task_id": "9396f93b-9dfb-48fb-9e6b-75c3a6ae7edf",
                   "status": "PROCESS_COMPLETE",
                   "is_search_all": true,
                   "search_all_status": "SEARCH_ALL_COMPLETE",
                   "aggregated_results": [
                       {
                           "tpa_name": "TPA002",
                           "status": "found",
                           "data": {
                               "is_eligible": true,
                               "patient_info": {
                                   "policy_holder_name": "[PATIENT_NAME]"
                               }
                           }
                       }
                   ],
                   "total_tpas_checked": 1,
                   "found_results": 1,
                   "created_at": "2025-08-29T08:31:32.261877",
                   "updated_at": "2025-08-29T08:32:12.192226"
               },
               {
                   "task_id": "f334c948-8b90-4d37-8d40-80808a409f01",
                   "status": "NAVIGATING_WEBSITE",
                   "is_search_all": true,
                   "search_all_status": "SEARCH_ALL_PROCESSING",
                   "aggregated_results": [],
                   "total_tpas_checked": 0,
                   "found_results": 0,
                   "created_at": "2025-08-29T09:00:00.000000",
                   "updated_at": "2025-08-29T09:00:05.123456"
               }
           ]
       }
   }