.. _health_check:

(GET) Health Check
==================

**Endpoint**

.. code-block:: bash

   GET /v2/api-integration/health

**Description**

Checks the health status of the API. This is a simple endpoint to verify that the API is running and accessible.

**Successful Response Example**

.. code-block:: json

   {
       "status": "healthy",
       "timestamp": "2025-06-10T03:55:41.123710"
   }