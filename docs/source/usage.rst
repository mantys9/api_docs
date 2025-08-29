.. _usage:

Usage
=====

This guide provides everything you need to get started with the Mantys API for eligibility checks.

.. contents::
   :local:

---

Getting Started
---------------

The Mantys Healthcare System API is a RESTful API that allows you to check patient insurance eligibility across multiple Third Party Administrators (TPAs) and healthcare providers in the UAE and broader Middle East region.

**Base URL**

.. code-block:: text

   https://prod-uae.api.mantys.in

**Authentication**

All API requests require authentication. To get your API key and credentials, please contact Kriti at kriti@mantys.io.

The following headers are required for all requests:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Header
     - Description
   * - ``x-api-key``
     - Your API key (e.g., ``Bearer api_aster_...``)
   * - ``x-client-id``
     - Your client identifier (e.g., ``mantys``)
   * - ``x-clinic-id``
     - The clinic identifier for your facility.
   * - ``Content-Type``
     - ``application/json``

---

Quick Start
-----------

Here's a simple eligibility check example that creates a task to be processed.

.. code-block:: bash

   curl -X POST "https://prod-uae.api.mantys.in/v2/api-integration/create-task" \
     -H "x-api-key: Bearer YOUR_API_KEY" \
     -H "x-client-id: mantys" \
     -H "x-clinic-id: 2a82dd66-5137-454f-bdc9-07d7c2c6dbbf" \
     -H "Content-Type: application/json" \
     -d '{
       "id_value": "784-XXXX-XXXXXXX-X",
       "id_type": "EMIRATESID",
       "tpa_name": "TPA002",
       "visit_type": "OUTPATIENT"
     }'

**Response**

The response will contain a ``task_id`` which you can use to query the task's status and result.

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

To retrieve the results, you will need to poll the ``/eligibility-result/{task_id}`` endpoint. See the :ref:`api_reference` for more details.






.. _error_handling:

---

Error Handling
--------------

The API uses standard HTTP status codes:

- **200 OK**: Request successful
- **400 Bad Request**: Invalid request format  
- **401 Unauthorized**: Invalid or missing API key
- **404 Not Found**: Patient not found
- **500 Internal Server Error**: Server error

**Error Response Format**

.. code-block:: json

   {
     "error": {
       "code": "INVALID_REQUEST",
       "message": "The request was malformed"
     }
   }

---

Best Practices
--------------

**Validate Input Data**
   Always validate patient and provider data on your end before sending it to the API. This reduces errors and ensures that required fields (like ``id_value``, ``id_type``, and ``tpa_name``) are present and correctly formatted.

**Implement Robust Error Handling**
   Build logic to handle the different HTTP status codes returned by the API. This includes gracefully managing `4xx` client-side errors (like invalid requests) and `5xx` server-side errors. Refer to the :ref:`error_handling` section for details.

**Use Provider-Specific Payloads**
   Different TPAs and insurance providers may require slightly different payload structures or have unique ``visit_type`` options. Always consult the :ref:`provider_payloads` documentation to ensure you are sending the correct data for the specified provider.

**Secure Your API Keys**
   Your API key is a secret and should be treated as such. Never expose it in client-side code (like a web browser or mobile app). All API calls should be made from a secure backend server where your key can be stored safely.

---

Next Steps
----------

- Review :ref:`api_reference` for detailed endpoint documentation
- Check :ref:`provider_payloads` for provider-specific request formats
- Explore :ref:`use_cases` for real-world examples
- Study :ref:`data_models` for complete response schemas