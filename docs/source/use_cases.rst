.. _use_cases:

Use Cases
=========

This section provides practical examples and real-world integration scenarios for the Mantys API.

.. contents::
   :local:

---

Common Integration Patterns
---------------------------

**Clinic Management System Integration**

Most clinic management systems integrate with the API during patient check-in to verify insurance eligibility before treatment.

**Typical Workflow**

1. Patient provides Emirates ID or insurance card.
2. System calls the API (``POST /create-task``) with patient details and visit type.
3. The API returns a ``task_id``.
4. The system polls the ``GET /eligibility-result/{task_id}`` endpoint until the status is ``PROCESS_COMPLETE``.
5. The system processes the final eligibility response.
6. Staff reviews copay requirements and network status.
7. Treatment proceeds with confirmed coverage details.

**Benefits**

- Asynchronous processing for non-blocking workflows.
- Real-time eligibility verification.
- Automatic copay calculation.
- Network coverage validation.
- Reduced claim rejections.

---

Use Case 1: DHPO Entry Optimization
------------------------------------

**Scenario**

A patient presents with an Emirates ID that has an existing entry in the Dubai Health Partnership Office (DHPO) database with valid insurance coverage.

**API Behavior**

When a patient's Emirates ID has a valid DHPO entry, the API automatically optimizes the search process. The final eligibility result will have ``is_search_all`` set to ``false``, and the result is returned much faster.

**Sample Request**

.. code-block:: bash

   curl -X POST "https://prod-uae.api.mantys.in/v2/api-integration/create-task" \
     -H "x-api-key: Bearer YOUR_API_KEY" \
     -H "x-client-id: mantys" \
     -H "x-clinic-id: 2a82dd66-5137-454f-bdc9-07d7c2c6dbbf" \
     -H "Content-Type: application/json" \
     -d '{
       "phone": "971-X",
       "id_type": "EMIRATESID",
       "id_value": "784-XXXX-XXXXXXX-X",
       "tpa_name": "INS010",
       "payerName": "",
       "doctorName": "DHA-P-0133260",
       "visit_type": "OUTPATIENT"
     }'

**Sample Response (from polling)**

Once the task is complete, the result will look like this:

.. code-block:: json

   {
       "task_id": "b1a35a89-f198-4429-a21d-65d0b0862a43",
       "status": "PROCESS_COMPLETE",
       "is_search_all": false,
       "eligibility_result": {
           "search_id": "784-XXXX-XXXXXXX-X",
           "data_dump": {
               "tpa": "INS010",
               "data": {
                   "is_eligible": true
               }
           }
       }
   }

---

Use Case 2: Multi-Provider Search
----------------------------------

**Scenario**

A patient has insurance but is unsure which TPA/provider manages their coverage. The API can search across multiple providers to find a match.

**API Behavior**

To initiate a multi-provider search, you can use one of the special ``tpa_name`` values:

- ``DHPO``: Searches for providers under the DHPO network.
- ``RIYATI``: Searches for providers under the Riyati network.
- ``BOTH``: Searches across both DHPO and Riyati networks.

The API will attempt to find the patient's coverage across all included providers. This process may take longer than a direct search.

**Sample Request**

This example uses ``BOTH`` to search across all available providers.

.. code-block:: bash

   curl -X POST "https://prod-uae.api.mantys.in/v2/api-integration/create-task" \
     -H "x-api-key: Bearer YOUR_API_KEY" \
     -H "x-client-id: mantys" \
     -H "x-clinic-id: 2a82dd66-5137-454f-bdc9-07d7c2c6dbbf" \
     -H "Content-Type: application/json" \
     -d '{
       "id_value": "784-XXXX-XXXXXXX-X",
       "id_type": "EMIRATESID",
       "tpa_name": "BOTH",
       "visit_type": "OUTPATIENT"
     }'

**Sample Response (from polling)**

If a match is found, the response will indicate the correct TPA that was identified.

.. code-block:: json

   {
       "task_id": "c2b46b90-f209-4430-b22e-76e1c0973b54",
       "status": "PROCESS_COMPLETE",
       "is_search_all": true,
       "eligibility_result": {
           "search_id": "784-XXXX-XXXXXXX-X",
           "data_dump": {
               "tpa": "TPA004",
               "data": {
                   "is_eligible": true
               }
           }
       }
   }



---

Related Documentation
---------------------

- :ref:`api_reference` - Complete API endpoint documentation
- :ref:`provider_payloads` - Provider-specific request formats
- :ref:`data_models` - Detailed response schema documentation
- :ref:`usage` - Basic integration guide
