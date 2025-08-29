.. _create_task:

(POST) Create Eligibility Task
==============================

**Endpoint**

.. code-block:: bash

   POST /v2/api-integration/create-task

**Description**

Creates a new eligibility verification task for a single patient. This is the primary endpoint for initiating an eligibility check. The system will process the task asynchronously.

.. note::
   Providing a specific ``tpa_name`` (e.g., ``TPA002``) will perform a direct eligibility check with that provider. Using a special value like ``BOTH`` or ``SEARCH_ALL`` will initiate a multi-provider search to find a match, which may take longer to complete.

**Request Body**

The request body must contain the patient and visit details. See :ref:`provider_payloads` for provider-specific examples.

.. list-table::
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
     - **Required.** The TPA code. See :ref:`provider_payloads` for the list of available TPAs.
   * - ``visit_type``
     - String
     - **Required.** The type of visit.
   * - ``extra_args``
     - Object
     - Optional. Additional parameters with ``title`` and ``value`` fields.
   * - ``doctorName``
     - String
     - Optional. Name of the doctor.
   * - ``payerName``
     - String
     - Optional. Name of the payer.

**Request Example**

.. code-block:: json

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
   }

**Request Example (Search All)**

To perform a multi-provider search, use a special ``tpa_name`` like ``BOTH``.

.. code-block:: json

   {
       "id_value": "784-XXXX-XXXXXXX-X",
       "id_type": "EMIRATESID",
       "tpa_name": "BOTH",
       "visit_type": "OUTPATIENT",
       "extra_args": {
           "title": "",
           "value": ""
       },
       "doctorName": "",
       "payerName": ""
   }

**Successful Response Example**

The response contains a ``task_id`` which is used to poll for the result.

.. code-block:: json

   {
       "success": true,
       "message": "Task created successfully",
       "data": {
           "task_id": "b3c3527d-a967-4bc1-8cc3-787227bbb4bb",
           "status": "pending",
           "organization_api_task_db": {
               "task_id_in_db": "b3c3527d-a967-4bc1-8cc3-787227bbb4bb",
               "task_id_in_celery": "b3c3527d-a967-4bc1-8cc3-787227bbb4bb",
               "status": "IN_QUEUE"
           }
       }
   }

**Successful Response Example (Search All)**

This is an example of a response when using a broad search parameter like ``BOTH`` for the ``tpa_name``.

.. code-block:: json

   {
       "success": true,
       "message": "Task created successfully",
       "data": {
           "task_id": "f334c948-8b90-4d37-8d40-80808a409f01",
           "status": "pending",
           "organization_api_task_db": {
               "task_id_in_db": "f334c948-8b90-4d37-8d40-80808a409f01",
               "task_id_in_celery": "f334c948-8b90-4d37-8d40-80808a409f01",
               "status": "SEARCH_ALL_PROCESSING"
           },
           "is_search_all": true,
           "search_all_status": "SEARCH_ALL_PROCESSING"
       }
   }