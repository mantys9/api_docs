.. _data_models:

Data Models
===========

This section provides a complete and detailed specification for all data structures used in the Mantys API. Understanding these models is crucial for successful integration, as they define the structure of requests you send and responses you receive.

.. contents::
   :local:

---

Request Bodies
--------------

Create Task Request (`POST /create-task`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The request body for creating a single eligibility verification task. This model is used by the :ref:`create_task` endpoint.

.. list-table:: Create Task Request Parameters
   :widths: 20 15 65
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``id_value``
     - String
     - **Required.** The patient's ID number (e.g., Emirates ID, Card Number).
   * - ``id_type``
     - String
     - **Required.** Type of ID: ``EMIRATESID``, ``CARDNUMBER``, ``DHAMEMBERID``, ``POLICYNUMBER``.
   * - ``tpa_name``
     - String
     - **Required.** The TPA (Third Party Administrator) code (e.g., ``TPA002``).
   * - ``visit_type``
     - String
     - **Required.** Type of visit, which varies by provider (e.g., ``OUTPATIENT``).
   * - ``phone``
     - String
     - *Optional.* The patient's phone number (format: "971-X").
   * - ``doctorName``
     - String
     - *Optional.* Doctor's name or DHA ID.
   * - ``payerName``
     - String
     - *Optional.* Payer name (required for some providers like Nextcare with ``POLICYNUMBER``).
   * - ``name``
     - String
     - *Optional.* Patient's name (required for Nextcare with ``POLICYNUMBER``).
   * - ``extra_args``
     - Object
     - *Optional.* Special arguments for specific cases (e.g., maternity treatment).

---

Response Bodies
---------------

This section details the main response objects returned by the API.

Task Creation Response (`POST /create-task`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The immediate response received after successfully creating an eligibility task. This model is returned by the :ref:`create_task` endpoint.

.. list-table:: Task Creation Response Fields
   :widths: 20 15 65
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``success``
     - Boolean
     - Indicates if the task was created successfully.
   * - ``message``
     - String
     - A confirmation message (e.g., "Task created successfully").
   * - ``data.task_id``
     - String
     - The unique UUID for the created task. This ID is used to fetch the result.
   * - ``data.status``
     - String
     - The initial status of the task (e.g., "pending" or "IN_QUEUE").

---

Eligibility Result Response (`GET /v2/api-integration/eligibility-result/{task_id}`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The full response object returned when polling for a task result. This model is returned by the :ref:`get_task_status` endpoint.

.. list-table:: Eligibility Result Response Fields
   :widths: 20 15 65
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``task_id``
     - String
     - The unique identifier of the task.
   * - ``status``
     - String
     - The current status of the task. Final statuses are typically ``PROCESS_COMPLETE`` or ``failed``.
   * - ``is_search_all``
     - Boolean
     - Indicates if a comprehensive search was performed (``false`` for DHPO-optimized results).
   * - ``search_all_status``
     - String
     - The status of the multi-provider search (e.g., ``SEARCH_ALL_PROCESSING``, ``SEARCH_ALL_COMPLETE``). Only present when ``is_search_all`` is ``true``.
   * - ``eligibility_result``
     - Object
     - The detailed eligibility information object. Present on success for **normal** searches.
   * - ``aggregated_results``
     - Array
     - An array of result objects from each provider. Present on success for **"Search All"** tasks. Each object contains a ``data`` field with an :ref:`eligibility_data_dump_object`.
   * - ``request_dump``
     - Object
     - A copy of the original request payload.
   * - ``created_at``
     - String
     - Timestamp of when the task was created (ISO 8601).
   * - ``updated_at``
     - String
     - Timestamp of the last update to the task (ISO 8601).

---

Core Data Structures
--------------------

This section describes the reusable data objects that appear in various API responses.

.. _eligibility_data_dump_object:

Eligibility Data Dump Object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This object contains the complete, detailed results of an eligibility check from a single provider. It is the most important data structure in the API response.

It is found in one of two places:
- For a normal (single-provider) task, it is the value of the ``data_dump`` key within the ``eligibility_result`` object.
- For a "Search All" (multi-provider) task, it is the value of the ``data`` key within each object in the ``aggregated_results`` array.

.. list-table:: Eligibility Data Dump Fields
   :widths: 25 15 60
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``is_eligible``
     - Boolean
     - The primary eligibility status (``true`` or ``false``).
   * - ``patient_info``
     - Object
     - Contains patient demographic and policy information. See :ref:`patient_info_object`.
   * - ``policy_network``
     - Object
     - Contains details about the patient's insurance network and plan. See :ref:`policy_network_object`.
   * - ``copay_analysis``
     - Object
     - Contains details about copayments, deductibles, and special remarks. See :ref:`copay_analysis_object`.
   * - ``copay_details_to_fill``
     - Array
     - A detailed, provider-specific breakdown of copay and deductibles. See :ref:`copay_details_object`.
   * - ``new_version_of_copay_analysis``
     - Object
     - A standardized, structured breakdown of benefits and cost-sharing. See :ref:`new_copay_analysis_object`.
   * - ``referral_documents``
     - Array
     - An array of objects containing links to downloadable documents. See :ref:`referral_document_object`.
   * - ``failure_reason``
     - String
     - A description of why a task failed, if applicable. Can be ``null``.
   * - ``screenshot_key``
     - String
     - A link to a screenshot of the provider's portal page.
   * - ``was_identified_by_aggregator``
     - Boolean
     - Indicates if the provider was found via a multi-provider search.

.. _patient_info_object:

Patient Information Object
^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``patient_info`` object contains the following fields:

.. list-table:: Patient Info Fields
   :widths: 25 15 60
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``patient_id_info``
     - Object
     - Contains specific ID numbers like ``national_id``, ``identity_card``, and ``regulator_member_id``.
   * - ``policy_holder_name``
     - String
     - Name of the policy holder.
   * - ``patient_emirates_id``
     - String
     - The patient's UAE Emirates ID.
   * - ``policy_holder_dob``
     - String
     - Date of birth of the policy holder (e.g., "YYYY-MM-DD").
   * - ``policy_primary_member_id``
     - String
     - The primary member ID on the policy.
   * - ``policy_holder_gender``
     - String
     - Gender of the policy holder.
   * - ``policy_holder_relationship``
     - String
     - The patient's relationship to the policy holder. Can be ``null``.
   * - ``policy_holder_phone``
     - String
     - The policy holder's phone number.

.. _policy_network_object:

Policy Network Object
^^^^^^^^^^^^^^^^^^^^^

The ``policy_network`` object contains details about the insurance plan.

.. list-table:: Policy Network Fields
   :widths: 25 15 60
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``all_networks``
     - Array
     - An array of available network objects for the policy.
   * - ``policy_plan_name``
     - String
     - The name of the insurance plan (e.g., "CAT C - NEW").
   * - ``policy_authority``
     - String
     - The regulatory authority (e.g., "DHA", "DOH").
   * - ``start_date``
     - String
     - Policy start date (e.g., "YYYY-MM-DD").
   * - ``valid_upto``
     - String
     - Policy expiry date (e.g., "YYYY-MM-DD").
   * - ``payer_name``
     - String
     - The name of the insurance payer.
   * - ``is_vip``
     - String
     - Indicates if the policy is a VIP plan.
   * - ``is_gatekeeper``
     - String
     - Indicates if a gatekeeper is required.
   * - ``package_name``
     - String
     - The name of the insurance package. Can be ``null``.

.. _copay_analysis_object:

Copay Analysis Object
^^^^^^^^^^^^^^^^^^^^^

The ``copay_analysis`` object provides a summary of cost-sharing and policy remarks.

.. list-table:: Copay Analysis Fields
   :widths: 25 15 60
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``copay_details``
     - Array
     - A summarized list of copay details for different visit types.
   * - ``waiting_period``
     - String
     - Information on any waiting periods for coverage.
   * - ``special_remarks``
     - Array
     - An array of strings containing important notes about the policy.

.. _copay_details_object:

Copay Details Object
^^^^^^^^^^^^^^^^^^^^

The ``copay_details_to_fill`` object provides a detailed, service-level breakdown of cost-sharing.

.. list-table:: Copay Details Fields
   :widths: 25 20 55
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``name``
     - String
     - Visit category: "Outpatient", "Maternity", "Specialization", "Inpatient".
   * - ``values_to_fill``
     - Object
     - A container for service-specific copay objects.

.. _new_copay_analysis_object:

New Copay Analysis Object
^^^^^^^^^^^^^^^^^^^^^^^^^

The ``new_version_of_copay_analysis`` object provides a standardized, structured breakdown of benefits.

.. list-table:: New Copay Analysis Fields
   :widths: 25 15 60
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``benefits``
     - Array
     - A list of benefit objects, each detailing a specific coverage type. See :ref:`benefit_object`.
   * - ``policy_info``
     - Object
     - Contains policy period and jurisdiction information. See :ref:`policy_info_object_new`.
   * - ``general_remarks``
     - Array
     - An array of strings with general remarks about the policy.
   * - ``abbreviations_defined``
     - Array
     - An array of defined abbreviations used in the policy.

.. _benefit_object:

Benefit Object
^^^^^^^^^^^^^^

Each object in the ``benefits`` array contains the following fields:

.. list-table:: Benefit Object Fields
   :widths: 25 15 60
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``service_category_original``
     - String
     - The original service category as defined by the provider (e.g., "Chronic Out", "Laboratory").
   * - ``service_category_standardized``
     - String
     - The standardized service category name.
   * - ``coverage_status``
     - String
     - The coverage status for this service (e.g., "Covered").
   * - ``cost_sharing``
     - Array
     - An array of cost-sharing objects detailing copay/coinsurance information. See :ref:`cost_sharing_object`.
   * - ``limits``
     - String/null
     - Any limits applicable to this benefit category.
   * - ``remarks``
     - String/null
     - Specific remarks for this benefit category.
   * - ``conditions``
     - String/null
     - Conditions that apply to this benefit.

.. _cost_sharing_object:

Cost Sharing Object
^^^^^^^^^^^^^^^^^^^

Each object in the ``cost_sharing`` array contains detailed payment information:

.. list-table:: Cost Sharing Object Fields
   :widths: 25 15 60
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``context``
     - String
     - The context of the cost sharing (e.g., "General").
   * - ``citation``
     - String
     - The original text citation from the provider (e.g., "Laboratory: Co-Part: 20% Max(100 AED)").
   * - ``visit_type``
     - String
     - The type of visit (e.g., "Outpatient").
   * - ``visit_setting``
     - String
     - The setting of the visit (e.g., "Outpatient").
   * - ``copay_amount``
     - Number/null
     - Fixed copay amount, if applicable.
   * - ``copay_percentage``
     - Number/String/null
     - Copay percentage or "Covered" if fully covered.
   * - ``copay_currency``
     - String
     - Currency for copay amounts (e.g., "AED").
   * - ``copay_maximum_amount``
     - Number/null
     - Maximum copay amount per visit/service.
   * - ``copay_maximum_scope``
     - String/null
     - The scope/currency of the maximum copay (e.g., "AED").
   * - ``coinsurance_percentage``
     - Number/null
     - Coinsurance percentage, if different from copay.

.. _policy_info_object_new:

Policy Info Object (New Version)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``policy_info`` object in the new copay analysis contains:

.. list-table:: Policy Info Object Fields
   :widths: 25 15 60
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``policy_jurisdiction``
     - String
     - The regulatory jurisdiction (e.g., "DHA", "DOH").
   * - ``waiting_period``
     - String
     - Information about waiting periods (e.g., "Not Specified").
   * - ``waiting_period_citation``
     - String/null
     - Citation for waiting period information.
   * - ``policy_period_start``
     - Object
     - Policy start date with ``DD``, ``MM``, ``YYYY`` fields.
   * - ``policy_period_end``
     - Object
     - Policy end date with ``DD``, ``MM``, ``YYYY`` fields.
   * - ``beneficiary_start_date``
     - Object
     - When the beneficiary's coverage began with ``DD``, ``MM``, ``YYYY`` fields.

.. _referral_document_object:

Referral Document Object
^^^^^^^^^^^^^^^^^^^^^^^^

This object represents a downloadable document related to the eligibility check.

.. list-table:: Referral Document Fields
   :widths: 25 15 60
   :header-rows: 1

   * - Field
     - Type
     - Description
   * - ``id``
     - String
     - The document identifier (e.g., "claim_form").
   * - ``tag``
     - String
     - A human-readable name for the document (e.g., "Claim Form").
   * - ``s3_url``
     - String
     - The pre-signed URL to download the document.
