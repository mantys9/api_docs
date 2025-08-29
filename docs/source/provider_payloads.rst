.. _provider_payloads:

Provider Payloads
=================

This section provides a comprehensive guide to all supported provider payloads for use in API requests. These payloads represent various entities, including Third-Party Administrators (TPAs) and insurance providers.

.. contents::
   :local:
   :depth: 2

.. note::
   The term "TPA" is used generically in the API for historical reasons, but it encompasses a broader range of provider types including insurance companies and health networks.
   
   When a provider has **Visit Types: None**, pass an empty string ("") for the ``visit_type`` field in your API request.

**Example for providers with no visit types:**

.. code-block:: json

   {
       "tpa_name": "TPA008",
       "id_value": "784-XXXX-XXXXXXX-X",
       "id_type": "EMIRATESID",
       "visit_type": ""
   }

Quick Reference
---------------

When making an API request that requires specifying a provider:

1. **Choose the provider**: Use the ``tpa_name`` value from the provider tables below
2. **Find your provider section**: Look up your specific provider in the :ref:`provider_requirements` section
3. **Check requirements**: Review the supported ID types, visit types, and required fields
4. **Reference ID types**: Use the :ref:`id_types` section for ID type descriptions if needed
5. **Reference visit types**: Use the :ref:`visit_types` section for visit type descriptions if needed

.. _special_payloads:

Special Payloads
----------------

These payloads are used for special cases, such as when the insurance provider is unknown.

.. list-table::
   :widths: 70 30
   :header-rows: 1

   * - Description
     - ``tpa_name``
   * - Unsure of Insurance (DHPO)
     - ``DHPO``
   * - Unsure of Insurance (Riyati)
     - ``RIYATI``
   * - Unsure of Insurance (Both)
     - ``BOTH``

Third-Party Administrators (TPAs)
---------------------------------

.. list-table::
   :widths: 70 30
   :header-rows: 1

   * - TPA Name
     - ``tpa_name``
   * - AAFIYA MEDICAL BILLING SERVICES L.L.C (TPA026)
     - ``TPA026``
   * - AL MADALLAH HEALTHCARE MANAGEMENT (TPA003)
     - ``TPA003``
   * - ECARE INTERNATIONAL MEDICAL BILLING SERVICES DUBAI (TPA029)
     - ``TPA029``
   * - FMC NETWORK UAE MANAGEMENT CONSULTANCY (TPA010)
     - ``TPA010``
   * - INAYAH (TPA008)
     - ``TPA008``
   * - LIFELINE TPA (Khat Al Haya Management of Health Insurance Claims L.L.C) (TPA037)
     - ``TPA037``
   * - MEDNET UAE FZ LLC Dubai (TPA036)
     - ``TPA036``
   * - NAS ADMINISTRATION SERVICES LIMITED (TPA004)
     - ``TPA004``
   * - NEURON LLC (TPA001)
     - ``TPA001``
   * - NEXTCARE ARAB GULF HEALTH SERVICES (TPA002)
     - ``TPA002``
   * - ROYAL HEALTH CARE SERVICES L.L.C (TPA026)
     - ``TPA026``

Insurance Providers
-------------------

.. list-table::
   :widths: 70 30
   :header-rows: 1

   * - Insurance Provider Name
     - ``tpa_name``
   * - ABU DHABI NATIONAL INSURANCE COMPANY | Adnic (INS017)
     - ``INS017``
   * - AL BUHAIRA NATIONAL INSURANCE COMPANY (INS020)
     - ``INS020``
   * - AXA INSURANCE - GULF (INS010)
     - ``INS010``
   * - Daman- National Health Insurance Company (INS026)
     - ``INS026``
   * - Daman- National Health Insurance Company - MOH (INS026__MOH)
     - ``INS026__MOH``
   * - Healthnet- National General Insurance Company | NGI (INS038)
     - ``INS038``
   * - OMAN / SUKOON Insurance Company (INS012)
     - ``INS012``
   * - Saico (INS015)
     - ``INS015``

.. _id_types:

ID Types Reference
------------------

The ``id_type`` field specifies the type of identification used for the patient. Below are the available ID types:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - ID Type
     - Description
   * - ``EMIRATESID``
     - Emirates ID number
   * - ``CARDNUMBER``
     - Insurance card number / Member ID
   * - ``DHAMEMBERID``
     - Dubai Health Authority Member ID
   * - ``POLICYNUMBER``
     - Insurance policy number
   * - ``PASSPORT``
     - Passport number

.. _visit_types:

Visit Types Reference
---------------------

The ``visit_type`` field specifies the type of medical visit. Below are the available visit types:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Visit Type
     - Description
   * - ``OUTPATIENT``
     - A standard outpatient visit.
   * - ``INPATIENT``
     - An inpatient hospital stay.
   * - ``EMERGENCY``
     - An emergency room visit.
   * - ``DENTAL``
     - A dental visit.
   * - ``OPTICAL``
     - An optical or vision-related visit.
   * - ``MATERNITY``
     - A maternity-related visit.
   * - ``TELEHEALTH``
     - A telemedicine/teleconsultation visit.
   * - ``FREE_FOLLOWUP``
     - A free follow-up visit.
   * - ``DIAGNOSTIC``
     - Diagnostic testing services.
   * - ``PHYSIOTHERAPY``
     - Physiotherapy services.
   * - ``DENTAL_SERVICES``
     - Dental services.
   * - ``PHARMACY``
     - Pharmacy services.
   * - ``HOMECARE``
     - Home care services.
   * - ``REHABILITATION``
     - Rehabilitation services.
   * - ``DAYCARE``
     - Day care services.
   * - ``ULTRASOUND``
     - Ultrasound services.
   * - ``OTHER_OP``
     - Other outpatient services.
   * - ``DAYCASE``
     - Day case procedures.
   * - ``PSYCHIATRY``
     - Psychiatric services.
   * - ``WELLNESS``
     - Wellness services.
   * - ``LIFE``
     - Life insurance related visits.
   * - ``TRAVEL_INSURANCE``
     - Travel insurance related visits.
   * - ``CHRONIC_OUT``
     - Chronic outpatient visits.

.. note::
   Each provider supports different visit types. Most providers support the standard visit types (OUTPATIENT, INPATIENT, EMERGENCY), while some have additional or specialized visit types as listed in their individual sections.

.. warning::
   Using an unsupported visit type will result in API errors. Always verify the provider-specific requirements before implementation.

---

.. _provider_requirements:

Provider-Specific Requirements
------------------------------

Each provider has specific requirements for ID types, fields, and visit types. Below are the detailed requirements for each provider.

TPA001 (Neuron LLC)
^^^^^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``, ``DHAMEMBERID``

**Visit Types**: ``OUTPATIENT``, ``INPATIENT``, ``DENTAL``, ``OPTICAL``, ``MATERNITY``, ``PSYCHIATRY``, ``WELLNESS``

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``, ``extra_args`` (for MATERNITY visits with trimester information)

**Optional Fields**: None

TPA002 (Nextcare)
^^^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``, ``DHAMEMBERID``, ``POLICYNUMBER``

**Visit Types**: ``INPATIENT``, ``OUTPATIENT``, ``DENTAL``, ``LIFE``, ``OPTICAL``, ``TRAVEL_INSURANCE``, ``CHRONIC_OUT``, ``EMERGENCY``, ``MATERNITY``

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``, ``name`` (when using Policy Number), ``payerName`` (when using Policy Number)

**Optional Fields**: ``doctorName``

TPA003 (Al Madallah)
^^^^^^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``

**Visit Types**: ``OUTPATIENT``, ``INPATIENT``, ``MATERNITY``, ``DENTAL``, ``OPTICAL``, ``PSYCHIATRY``

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``, ``name`` (when ID type is Member ID)

**Optional Fields**: None

TPA004 (NAS Administration)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``, ``DHAMEMBERID``

**Visit Types**: ``OUTPATIENT``, ``INPATIENT``, ``DENTAL``, ``OPTICAL``, ``MATERNITY``, ``PSYCHIATRY``, ``WELLNESS``

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``, ``extra_args`` (for MATERNITY visits with trimester information)

**Optional Fields**: None

TPA008 (Inayah)
^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``

**Visit Types**: None

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``

**Optional Fields**: None

TPA010 (FMC Network)
^^^^^^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``, ``DHAMEMBERID``, ``PASSPORT``

**Visit Types**: ``OUTPATIENT``, ``INPATIENT``

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``

**Optional Fields**: None

TPA026 (Aafiya)
^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``

**Visit Types**: None

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``

**Optional Fields**: ``referralCode``

TPA029 (Ecare)
^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``

**Visit Types**: ``OUTPATIENT``, ``INPATIENT``

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``, ``phone``, ``serviceType``

**Optional Fields**: ``doctorName``

TPA036 (Mednet UAE)
^^^^^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``, ``DHAMEMBERID``

**Visit Types**: ``OUTPATIENT``, ``EMERGENCY``

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``

**Optional Fields**: ``is_emergency``

TPA037 (Lifeline TPA)
^^^^^^^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``, ``DHAMEMBERID``, ``POLICYNUMBER``

**Visit Types**: None

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``

**Optional Fields**: None

INS010 (AXA Insurance)
^^^^^^^^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``, ``DHAMEMBERID``

**Visit Types**: None

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``

**Optional Fields**: None

INS012 (Oman/Sukoon)
^^^^^^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``

**Visit Types**: None

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``

**Optional Fields**: None

INS015 (Saico)
^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``

**Visit Types**: None

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``

**Optional Fields**: None

INS017 (Adnic)
^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``, ``DHAMEMBERID``

**Visit Types**: None

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``

**Optional Fields**: None

INS020 (Al Buhaira)
^^^^^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``

**Visit Types**: None

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``

**Optional Fields**: None

INS026 (Daman)
^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``

**Visit Types**: ``OUTPATIENT``, ``INPATIENT``, ``TELEHEALTH``, ``FREE_FOLLOWUP``, ``DIAGNOSTIC``, ``PHYSIOTHERAPY``, ``DENTAL_SERVICES``, ``PHARMACY``, ``HOMECARE``, ``REHABILITATION``, ``DAYCARE``, ``ULTRASOUND``, ``OTHER_OP``

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``, ``doctorName``, ``pod_id`` (for specific clinic)

**Optional Fields**: ``pod_id``

INS026__MOH (Daman - MOH)
^^^^^^^^^^^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``

**Visit Types**: ``OUTPATIENT``, ``INPATIENT``, ``TELEHEALTH``, ``FREE_FOLLOWUP``, ``DIAGNOSTIC``, ``PHYSIOTHERAPY``, ``DENTAL_SERVICES``, ``PHARMACY``, ``HOMECARE``, ``REHABILITATION``, ``DAYCARE``, ``ULTRASOUND``, ``OTHER_OP``

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``, ``doctorName``

**Optional Fields**: ``pod_id``

INS038 (Healthnet/NGI)
^^^^^^^^^^^^^^^^^^^^^^

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``, ``DHAMEMBERID``

**Visit Types**: ``OUTPATIENT``, ``INPATIENT``, ``DAYCASE``

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``

**Optional Fields**: None

Special Multi-Provider Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

BOTH
""""

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``

**Visit Types**: ``OUTPATIENT``, ``INPATIENT``, ``DAYCASE``, ``MATERNITY``, ``DENTAL``, ``OPTICAL``, ``PSYCHIATRY``, ``WELLNESS``, ``LIFE``, ``TRAVEL_INSURANCE``, ``CHRONIC_OUT``, ``EMERGENCY``

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``, ``name`` (when ID type is Member ID)

**Optional Fields**: ``doctorName``

DHPO
""""

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``

**Visit Types**: ``OUTPATIENT``, ``INPATIENT``, ``DAYCASE``, ``MATERNITY``, ``DENTAL``, ``OPTICAL``, ``PSYCHIATRY``, ``WELLNESS``, ``LIFE``, ``TRAVEL_INSURANCE``, ``CHRONIC_OUT``, ``EMERGENCY``

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``, ``name`` (when ID type is Member ID)

**Optional Fields**: ``doctorName``

RIYATI
""""""

**ID Types**: ``EMIRATESID``, ``CARDNUMBER``

**Visit Types**: ``OUTPATIENT``, ``INPATIENT``, ``DAYCASE``, ``MATERNITY``, ``DENTAL``, ``OPTICAL``, ``PSYCHIATRY``, ``WELLNESS``, ``LIFE``, ``TRAVEL_INSURANCE``, ``CHRONIC_OUT``, ``EMERGENCY``

**Required Fields**: ``id_value``, ``id_type``, ``tpa_name``, ``visit_type``, ``name`` (when ID type is Member ID)

**Optional Fields**: ``doctorName``


---


