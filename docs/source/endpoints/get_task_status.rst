.. _get_task_status:

(GET) Get Eligibility Task Status
==================================

**Endpoint**

.. code-block:: bash

   GET /v2/api-integration/eligibility-result/{task_id}

**Description**

Retrieves the status and results of a specific eligibility task. You should poll this endpoint after creating a task until the ``status`` is ``PROCESS_COMPLETE``. The task will go through several interim statuses before completion.

**Path Parameters**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Parameter
     - Description
   * - ``task_id``
     - The unique identifier of the task.

**Response Examples**
---------------------

The structure of the response object differs slightly depending on whether you initiated a normal (single TPA) or a "Search All" (multi-TPA) task. For a complete breakdown of all fields and data structures in these responses, please refer to the :ref:`data_models` documentation.

Normal Task Examples
^^^^^^^^^^^^^^^^^^^^

These examples show the typical lifecycle of a task created with a specific ``tpa_name``.

**NAVIGATING_WEBSITE (In Progress)**

The initial status while the system navigates the provider's portal.

.. code-block:: json

   {
       "task_id": "6193fa12-8915-4854-838d-061f8a0fe605",
       "status": "NAVIGATING_WEBSITE",
       "request_dump": {
           "id_type": "EMIRATESID",
           "id_value": "784-XXXX-XXXXXXX-X",
           "tpa_name": "TPA002"
       },
       "created_at": "2025-06-05T21:16:21.958547",
       "updated_at": "2025-06-05T21:16:22.369894"
   }

**EXTRACTING_DATA (In Progress)**

The status when data is being extracted. The ``interim_results`` may contain partial data, such as document links.

.. code-block:: json

   {
       "task_id": "6193fa12-8915-4854-838d-061f8a0fe605",
       "status": "EXTRACTING_DATA",
       "interim_results": {
           "tpa_name": "TPA002",
           "screenshot_key": "https://s3.me-central-1.amazonaws.com/...",
           "referral_documents": [
               {
                   "id": "member_eligibility_document",
                   "tag": "Member Eligibility Document",
                   "s3_url": "https://s3.me-central-1.amazonaws.com/..."
               }
           ]
       }
   }

**PROCESS_COMPLETE (Success)**

The final status for a successful eligibility check. The ``eligibility_result`` object contains the full details.

.. code-block:: json

   {
       "task_id": "a4c0066b-af5c-4c12-b8e7-ed139cab9171",
       "status": "PROCESS_COMPLETE",
       "request_dump": {
           "id_type": "EMIRATESID",
           "id_value": "784-YYYY-YYYYYYY-Y",
           "tpa_name": "TPA002"
       },
       "is_search_all": false,
       "created_at": "2025-08-29T09:32:17.432050",
       "updated_at": "2025-08-29T09:32:55.264733",
       "eligibility_result": {
           "search_id": "784-YYYY-YYYYYYY-Y",
           "data_dump": {
               "tpa": "TPA002",
               "data": {
                   "is_eligible": true,
                   "patient_info": {
                       "policy_holder_name": "[PATIENT_NAME]",
                       "patient_emirates_id": "784-YYYY-YYYYYYY-Y"
                   },
                   "policy_network": {
                       "policy_plan_name": null,
                       "payer_name": "ORIENT INSURANCE PJSC - INS008",
                       "all_networks": [
                           {
                               "network": "GN+ (OP)",
                               "network_value": "GN+"
                           }
                       ]
                   },
                   "copay_details_to_fill": [
                        {
                            "name": "Outpatient",
                            "values_to_fill": {
                                "LAB": {
                                    "copay": "20.0",
                                    "deductible": "0"
                                }
                            }
                        }
                   ],
                   "referral_documents": [
                        {
                            "id": "claim_form",
                            "tag": "Claim Form",
                            "s3_url": "https://s3.me-central-1.amazonaws.com/..."
                        }
                   ]
               }
           }
       }
   }

**PROCESS_COMPLETE (Failure: Member Not Found)**

The final status when the task is complete, but the patient could not be found.

.. code-block:: json

   {
       "task_id": "9eec1edd-99ce-4ff6-b5ce-2b714d137170",
       "status": "PROCESS_COMPLETE",
       "request_dump": {
           "id_value": "784-ZZZZ-ZZZZZZZ-Z",
           "tpa_name": "TPA002"
       },
       "eligibility_result": {
           "data_dump": {
               "status": "member_not_found",
               "message": "`This beneficiary is Invalid` was seen",
               "error_type": "MemberNotFoundError"
           }
       }
   }

Search All Task Examples
^^^^^^^^^^^^^^^^^^^^^^^^

These examples show the lifecycle of a task created with a multi-provider ``tpa_name`` like ``BOTH``.

**NAVIGATING_WEBSITE (Search All In Progress)**

The status for a multi-provider search task that is in progress.

.. code-block:: json

   {
       "task_id": "9396f93b-9dfb-48fb-9e6b-75c3a6ae7edf",
       "status": "NAVIGATING_WEBSITE",
       "request_dump": {
           "id_type": "EMIRATESID",
           "id_value": "784-YYYY-YYYYYYY-Y",
           "tpa_name": "BOTH"
       },
       "is_search_all": true,
       "search_all_status": "SEARCH_ALL_PROCESSING",
       "aggregated_results": [],
       "total_tpas_checked": 0,
       "found_results": 0,
       "created_at": "2025-08-29T08:31:32.261877",
       "updated_at": "2025-08-29T08:31:32.744330"
   }

**EXTRACTING_DATA (Search All In Progress)**

The status when data is being extracted during a multi-provider search.

.. code-block:: json

   {
       "task_id": "6dd12907-ecb9-4ee1-a915-41554fa75b84",
       "status": "EXTRACTING_DATA",
       "request_dump": {
           "id_type": "EMIRATESID",
           "id_value": "784-YYYY-YYYYYYY-Y",
           "tpa_name": "BOTH"
       },
       "is_search_all": true,
       "search_all_status": "SEARCH_ALL_PROCESSING",
       "aggregated_results": [],
       "total_tpas_checked": 0,
       "found_results": 0,
       "created_at": "2025-08-29T09:35:49.661474",
       "updated_at": "2025-08-29T09:36:14.259707"
   }

**PROCESS_COMPLETE (Success - Search All)**

The final status for a successful multi-provider search. The ``aggregated_results`` array contains the detailed eligibility information.

.. code-block:: json

   {
       "task_id": "6dd12907-ecb9-4ee1-a915-41554fa75b84",
       "status": "PROCESS_COMPLETE",
       "request_dump": {
           "id_type": "EMIRATESID",
           "id_value": "784-YYYY-YYYYYYY-Y",
           "tpa_name": "BOTH"
       },
       "is_search_all": true,
       "search_all_status": "SEARCH_ALL_COMPLETE",
       "aggregated_results": [
           {
               "tpa_name": "TPA002",
               "status": "found",
               "data": {
                   "is_eligible": true,
                   "patient_info": {
                       "policy_holder_name": "[PATIENT_NAME]",
                       "patient_emirates_id": "784-YYYY-YYYYYYY-Y"
                   },
                   "copay_analysis": {
                       "copay_details": [
                           {
                               "remarks": "Citation: Chronic Out : Co-Part: 20% Max(100 AED) | \n\n ",
                               "visit_type": "Chronic Out"
                           }
                       ],
                       "special_remarks": []
                   },
                   "policy_network": {
                       "payer_name": "ORIENT INSURANCE PJSC - INS008",
                       "all_networks": [
                           {
                               "network": "GN+ (OP)",
                               "network_value": "GN+"
                           }
                       ]
                   },
                   "referral_documents": [
                       {
                           "id": "claim_form",
                           "tag": "Claim Form",
                           "s3_url": "https://s3.me-central-1.amazonaws.com/..."
                       }
                   ]
               }
           }
       ],
       "total_tpas_checked": 1,
       "found_results": 1,
       "created_at": "2025-08-29T09:35:49.661474",
       "updated_at": "2025-08-29T09:36:26.309358"
   }

