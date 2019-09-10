import datetime

# Extension Service

projectextensions = [
    {"workflowlevel2_uuid": "8132d789-9580-45ad-b22a-9384bce0eed6", "id": "not needed"},
    {"workflowlevel2_uuid": "6f015067-db3e-40be-8f87-8b20fa347752", "id": "not needed"},
    {"workflowlevel2_uuid": "9e3bda19-49e5-428a-a2cc-ef03153f14bb", "id": "not needed"},
    {"workflowlevel2_uuid": "7b504be7-36e3-4196-8c60-227b78f8ae96", "id": "not needed"},
    {"workflowlevel2_uuid": "999d0b08-759f-49d6-b121-e312c3ea17c5", "id": "not needed"},
]


# Location Service

profiletypes = [
    {"id": 79, "name": "billing", "is_global": True},
    {"id": 80, "name": "object", "is_global": True},
    {"id": 81, "name": "object_with_billing", "is_global": True},
]

siteprofiles = [
    {
        "uuid": "900498a7-8630-4c7c-9762-2447cc2178ce",
        "id": "900498a7-8630-4c7c-9762-2447cc2178ce",
        "country": "DE",
        "name": "Brandenburgische Straße 75, 12277 Berlin",
        "address_line1": "Brandenburgische Straße 75",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "12277",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "8132d789-9580-45ad-b22a-9384bce0eed6"
        ],
        "profiletype": 79
    }, #billing
    {
        "uuid": "485234bd-1bd6-49b9-81b9-7d84161b6b39",
        "id": "485234bd-1bd6-49b9-81b9-7d84161b6b39",
        "country": "DE",
        "name": "Lehmbruckstraße 12, 10245 Berlin",
        "address_line1": "Lehmbruckstraße 12",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "10245",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "999d0b08-759f-49d6-b121-e312c3ea17c5"
        ],
        "profiletype": 79
    }, #billing
    {
        "uuid": "5b04b3aa-f18e-416b-bf5b-bc9c86786159",
        "id": "5b04b3aa-f18e-416b-bf5b-bc9c86786159",
        "country": "DE",
        "name": "Ossastraße 44, 12045 Berlin",
        "address_line1": "Ossastraße 44",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "12045",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "6f015067-db3e-40be-8f87-8b20fa347752"
        ],
        "profiletype": 79
    }, #billing
    {
        "uuid": "551629e8-bb28-4734-a3e4-7edb239854b2",
        "id": "551629e8-bb28-4734-a3e4-7edb239854b2",
        "country": "DE",
        "name": "Tempelhofer Ufer 13, 10963 Berlin",
        "address_line1": "Tempelhofer Ufer 13",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "10963",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "9e3bda19-49e5-428a-a2cc-ef03153f14bb"
        ],
        "profiletype": 79
    }, #billing
    {
        "uuid": "5fa79e8b-599c-4a70-97ef-989f0c823e5d",
        "id": "5fa79e8b-599c-4a70-97ef-989f0c823e5d",
        "country": "DE",
        "name": "Urbanstraße 76, 10967 Berlin",
        "address_line1": "Urbanstraße 76",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "10967",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "7b504be7-36e3-4196-8c60-227b78f8ae96"
        ],
        "profiletype": 81
    }, #billing_with_object
    {
        "uuid": "6a69f3de-5640-409a-9f1d-4c6ce09b058b",
        "id": "6a69f3de-5640-409a-9f1d-4c6ce09b058b",
        "country": "DE",
        "name": "Genslerstraße 85, 14193 Berlin",
        "address_line1": "Genslerstraße 85",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "14193",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "37c40d1b-fe9b-4174-86aa-b77adbb739a8"
        ],
        "profiletype": 81
    }, #billing_with_object
    {
        "uuid": "589dc550-f65f-4a15-8280-10e9f203cce7",
        "id": "589dc550-f65f-4a15-8280-10e9f203cce7",
        "country": "DE",
        "name": "Leopoldstraße 30, 10247 Berlin",
        "address_line1": "Leopoldstraße 30",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "10247",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "fd98dce0-24f9-4f42-a0f7-febeff3b1174"
        ],
        "profiletype": 81
    }, #billing_with_object
    {
        "uuid": "4afb4661-918b-43b3-9555-5868b1922359",
        "id": "4afb4661-918b-43b3-9555-5868b1922359",
        "country": "DE",
        "name": "Waßmannsdorfer Chaussee 16, 13435 Berlin",
        "address_line1": "Waßmannsdorfer Chaussee 16",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "13435",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "3a63d21a-c111-405b-beaf-a3a0920bc9ac"
        ],
        "profiletype": 81
    }, #billing_with_object
    {
        "uuid": "25ef73fa-c00b-42ca-9d41-976527f3a4ae",
        "id": "25ef73fa-c00b-42ca-9d41-976527f3a4ae",
        "country": "DE",
        "name": "Septimerstraße 44, 13407 Berlin",
        "address_line1": "Septimerstraße 44",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "13407",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "a12e9ec2-e9cd-45e0-849c-ddbc74293bc9"
        ],
        "profiletype": 80
    }, #object
    {
        "uuid": "ebf80e7b-8c84-4bfd-90ca-fea7e18f08b3",
        "id": "ebf80e7b-8c84-4bfd-90ca-fea7e18f08b3",
        "country": "DE",
        "name": "Karl-Marx-Straße 55, 12043 Berlin",
        "address_line1": "Karl-Marx-Straße 55",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "12043",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "6ecf272c-b574-404e-a4eb-e9b9955c72ce"
        ],
        "profiletype": 80
    }, #object
    {
        "uuid": "7623adb5-ee81-4494-9c07-bbd3a1df4cb4",
        "id": "7623adb5-ee81-4494-9c07-bbd3a1df4cb4",
        "country": "DE",
        "name": "Ehrenstraße 44, 50672 Köln",
        "address_line1": "Ehrenstraße 44",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "50672",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "f0ad19c1-a09b-4e05-a96c-804d6ef3efa8"
        ],
        "profiletype": 81
    }, #billing_with_object
    {
        "uuid": "a5f42490-7493-4c1d-9cbf-fa1bce1f29b6",
        "id": "a5f42490-7493-4c1d-9cbf-fa1bce1f29b6",
        "country": "DE",
        "name": "Ehrenstraße 44, 50672 Köln",
        "address_line1": "Ehrenstraße 44",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "50672",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "5aa823a9-d3c6-4c6d-92fa-ec1e92c5ee3d"
        ],
        "profiletype": 80
    }, #object
    {
        "uuid": "e1c8d02e-067f-429d-9399-6646c92540e7",
        "id": "e1c8d02e-067f-429d-9399-6646c92540e7",
        "country": "DE",
        "name": "Kurfürstendamm 56, 10707 Berlin",
        "address_line1": "Kurfürstendamm 56",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "10707",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "af4c9679-5b2c-4f75-8014-f384bca3c5ef"
        ],
        "profiletype": 81
    }, #billing_with_object
    {
        "uuid": "d2aeaef8-c3c0-400a-b122-41fc28f7c06b",
        "id": "d2aeaef8-c3c0-400a-b122-41fc28f7c06b",
        "country": "DE",
        "name": "Lehrter Straße 68, 10557 Berlin",
        "address_line1": "Lehrter Straße 68",
        "address_line2": "",
        "address_line3": "",
        "address_line4": "",
        "postcode": "10557",
        "city": "Berlin",
        "administrative_level1": "",
        "administrative_level2": "",
        "administrative_level3": "",
        "administrative_level4": "",
        "latitude": "0.0000000000000000",
        "longitude": "0.0000000000000000",
        "notes": "",
        "workflowlevel2_uuid": [
            "7ac41a5c-0a4c-4fff-a1c7-92dc25bc7dba"
        ],
        "profiletype": 80
    }  #object
]


# CRM Service

contacts = [
    {
        "uuid": "61a012e5-d70b-4801-acb3-507b913fcd54",
        "id": "61a012e5-d70b-4801-acb3-507b913fcd54",
        "first_name": "Emalia",
        "last_name": "Whittle",
        "customer_type": "customer",
        "company": "Mustermann GmbH",
        "siteprofile_uuids": ["900498a7-8630-4c7c-9762-2447cc2178ce"],
        "emails": [{"type": "office", "email": "mustermann@mustermann.de"}],
        "phones": [{"type": "home", "number": "030376262666"}],
        "notes": None,
        "workflowlevel1_uuids": ["49a4c9d7-8b72-434b-8a48-24540f65a2f3"],
        "workflowlevel2_uuids": [
            "8132d789-9580-45ad-b22a-9384bce0eed6",
            "6f015067-db3e-40be-8f87-8b20fa347752",
        ],
        "contact_type": None,
    }, # Emalia
    {
        "uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "id": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "first_name": "Violet",
        "last_name": "Ferguson",
        "customer_type": "customer",
        "company": None,
        "siteprofile_uuids": ["485234bd-1bd6-49b9-81b9-7d84161b6b39"],
        "emails": [{"type": "office", "email": "mia.musterfrau@gmail.com"}],
        "phones": [{"type": "home", "number": "01721648387"}],
        "notes": None,
        "workflowlevel1_uuids": ["49a4c9d7-8b72-434b-8a48-24540f65a2f3"],
        "workflowlevel2_uuids": [
            "999d0b08-759f-49d6-b121-e312c3ea17c5",
        ],
        "contact_type": None,
    }, # Violet
    {
        "uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "id": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "first_name": "Kara",
        "last_name": "Barnes",
        "customer_type": "customer",
        "company": None,
        "siteprofile_uuids": ["5b04b3aa-f18e-416b-bf5b-bc9c86786159"],
        "emails": [{"type": "office", "email": "mia.musterfrau@gmail.com"}],
        "phones": [{"type": "home", "number": "01721648387"}],
        "notes": None,
        "workflowlevel1_uuids": ["49a4c9d7-8b72-434b-8a48-24540f65a2f3"],
        "workflowlevel2_uuids": [
            "6f015067-db3e-40be-8f87-8b20fa347752",
        ],
        "contact_type": None,
    }, # Kara
    {
        "uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "id": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "first_name": "Aleena",
        "last_name": "Wilkins",
        "customer_type": "customer",
        "company": None,
        "siteprofile_uuids": ["5fa79e8b-599c-4a70-97ef-989f0c823e5d"],
        "emails": [{"type": "office", "email": "mia.musterfrau@gmail.com"}],
        "phones": [{"type": "home", "number": "01721648387"}],
        "notes": None,
        "workflowlevel1_uuids": ["49a4c9d7-8b72-434b-8a48-24540f65a2f3"],
        "workflowlevel2_uuids": [
            "7b504be7-36e3-4196-8c60-227b78f8ae96",
        ],
        "contact_type": None,
    }, # Aleena
    {
        "uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "id": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "first_name": "Jasmin",
        "last_name": "Leonard",
        "customer_type": "customer",
        "company": None,
        "siteprofile_uuids": ["6a69f3de-5640-409a-9f1d-4c6ce09b058b"],
        "emails": [{"type": "office", "email": "mia.musterfrau@gmail.com"}],
        "phones": [{"type": "home", "number": "01721648387"}],
        "notes": None,
        "workflowlevel1_uuids": ["49a4c9d7-8b72-434b-8a48-24540f65a2f3"],
        "workflowlevel2_uuids": [
            "37c40d1b-fe9b-4174-86aa-b77adbb739a8",
        ],
        "contact_type": None,
    }, # Jasmin
    {
        "uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "id": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "first_name": "Lilly",
        "last_name": "Watson",
        "customer_type": "customer",
        "company": None,
        "siteprofile_uuids": ["589dc550-f65f-4a15-8280-10e9f203cce7"],
        "emails": [{"type": "office", "email": "mia.musterfrau@gmail.com"}],
        "phones": [{"type": "home", "number": "01721648387"}],
        "notes": None,
        "workflowlevel1_uuids": ["49a4c9d7-8b72-434b-8a48-24540f65a2f3"],
        "workflowlevel2_uuids": [
            "fd98dce0-24f9-4f42-a0f7-febeff3b1174",
        ],
        "contact_type": None,
    }, # Lilly
    {
        "uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "id": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "first_name": "Ema",
        "last_name": "Becker",
        "customer_type": "customer",
        "company": None,
        "siteprofile_uuids": ["551629e8-bb28-4734-a3e4-7edb239854b2"],
        "emails": [{"type": "office", "email": "mia.musterfrau@gmail.com"}],
        "phones": [{"type": "home", "number": "01721648387"}],
        "notes": None,
        "workflowlevel1_uuids": ["49a4c9d7-8b72-434b-8a48-24540f65a2f3"],
        "workflowlevel2_uuids": [
            "9e3bda19-49e5-428a-a2cc-ef03153f14bb",
            "a12e9ec2-e9cd-45e0-849c-ddbc74293bc9",
        ],
        "contact_type": None,
    }, # Ema
    {
        "uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "id": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "first_name": "Parag",
        "last_name": "Narvekar",
        "customer_type": "customer",
        "company": None,
        "siteprofile_uuids": ["4afb4661-918b-43b3-9555-5868b1922359"],
        "emails": [{"type": "office", "email": "mia.musterfrau@gmail.com"}],
        "phones": [{"type": "home", "number": "01721648387"}],
        "notes": None,
        "workflowlevel1_uuids": ["49a4c9d7-8b72-434b-8a48-24540f65a2f3"],
        "workflowlevel2_uuids": [
            "3a63d21a-c111-405b-beaf-a3a0920bc9ac",
            "6ecf272c-b574-404e-a4eb-e9b9955c72ce",
        ],
        "contact_type": None,
    }, # Parag
    {
        "uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "id": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "first_name": "Kutay",
        "last_name": "Yegül",
        "customer_type": "customer",
        "company": None,
        "siteprofile_uuids": ["7623adb5-ee81-4494-9c07-bbd3a1df4cb4"],
        "emails": [{"type": "office", "email": "mia.musterfrau@gmail.com"}],
        "phones": [{"type": "home", "number": "01721648387"}],
        "notes": None,
        "workflowlevel1_uuids": ["49a4c9d7-8b72-434b-8a48-24540f65a2f3"],
        "workflowlevel2_uuids": [
            "f0ad19c1-a09b-4e05-a96c-804d6ef3efa8",
            "5aa823a9-d3c6-4c6d-92fa-ec1e92c5ee3d",
        ],
        "contact_type": None,
    }, # Kutay
    {
        "uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "id": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "first_name": "Franziska",
        "last_name": "Holz",
        "customer_type": "customer",
        "company": None,
        "siteprofile_uuids": ["e1c8d02e-067f-429d-9399-6646c92540e7"],
        "emails": [{"type": "office", "email": "mia.musterfrau@gmail.com"}],
        "phones": [{"type": "home", "number": "01721648387"}],
        "notes": None,
        "workflowlevel1_uuids": ["49a4c9d7-8b72-434b-8a48-24540f65a2f3"],
        "workflowlevel2_uuids": [
            "af4c9679-5b2c-4f75-8014-f384bca3c5ef",
            "7ac41a5c-0a4c-4fff-a1c7-92dc25bc7dba",
        ],
        "contact_type": None,
    }, # Franziska
]

today = datetime.datetime.now().date()
delta = datetime.date.weekday(today)

Monday = today + datetime.timedelta(days=-delta)
Tuesday = today + datetime.timedelta(days=1-delta)
Wednesday = today + datetime.timedelta(days=2-delta)
Thursday = today + datetime.timedelta(days=3-delta)
Friday = today + datetime.timedelta(days=4-delta)


appointments = [
    {
        "uuid": "432aa435-f9ec-4984-87d3-31f1b2a9388e",
        "id": "432aa435-f9ec-4984-87d3-31f1b2a9388e",
        "notes": [
            {"id": 1971, "note": "", "type": 1},
            {"id": 1972, "note": "", "type": 3},
        ],
        "name": "Kupfer Appointment",
        "start_date": f"{Monday}T14:10:00+02:00",
        "end_date": f"{Monday}T16:10:00+02:00",
        "type": "consultation",
        "address": "Waßmannsdorfer Chaussee 16, 13435 Berlin",
        "siteprofile_uuid": "4afb4661-918b-43b3-9555-5868b1922359",
        "invitee_uuids": [],
        "workflowlevel2_uuids": ["3a63d21a-c111-405b-beaf-a3a0920bc9ac"],
        "contact_uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "summary": "",
    }, # Parag with billing
    {
        "uuid": "878db099-b8c1-4482-b4a8-11e26168c933",
        "id": "878db099-b8c1-4482-b4a8-11e26168c933",
        "notes": [
            {"id": 1973, "note": "Neuinstallation Vitodens 200", "type": 1},
            {"id": 1974, "note": "", "type": 3},
        ],
        "name": "Kupfer Appointment",
        "start_date": f"{Tuesday}T06:25:00+02:00",
        "end_date": f"{Tuesday}T08:25:00+02:00",
        "type": "installation",
        "address": "Ossastraße 44, 12045 Berlin",
        "siteprofile_uuid": "5b04b3aa-f18e-416b-bf5b-bc9c86786159",
        "invitee_uuids": [
            "44852b4a-4e80-448e-8936-71c4c294a1b7",
            "3418abb1-faff-4f38-86d9-606f3f542ef5",
            "40517e88-26cb-4b34-853f-ed383c1af0d6",
        ],
        "workflowlevel2_uuids": ["6f015067-db3e-40be-8f87-8b20fa347752"],
        "contact_uuid": "61a012e5-d70b-4801-acb3-507b913fcd54",
        "summary": "",
    }, # Aleena with billing
    {
        "uuid": "edeb1722-5b43-4eb0-ae52-b5598e40e704",
        "id": "edeb1722-5b43-4eb0-ae52-b5598e40e704",
        "notes": [
            {"id": 1976, "note": "", "type": 3},
            {"id": 1975, "note": "Bitte Standardwartung durchführen", "type": 1},
        ],
        "name": "Kupfer Appointment",
        "start_date": f"{Tuesday}T11:50:00+02:00",
        "end_date": f"{Tuesday}T14:10:00+02:00",
        "type": "maintenance",
        "address": "Tempelhofer Ufer 13, 10963 Berlin",
        "siteprofile_uuid": "551629e8-bb28-4734-a3e4-7edb239854b2",
        "invitee_uuids": ["44852b4a-4e80-448e-8936-71c4c294a1b7"],
        "workflowlevel2_uuids": ["9e3bda19-49e5-428a-a2cc-ef03153f14bb"],
        "contact_uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "summary": "",
    }, # Jasmin with billing
    {
        "uuid": "ed4c7e5a-5211-486e-a0ca-fcde746a8e2e",
        "id": "ed4c7e5a-5211-486e-a0ca-fcde746a8e2e",
        "notes": [
            {"id": 1977, "note": "Bitte Standardwartung durchführen", "type": 1},
            {"id": 1978, "note": "", "type": 3},
        ],
        "name": "Kupfer Appointment",
        "start_date": f"{Wednesday}T06:25:00+02:00",
        "end_date": f"{Thursday}T06:25:00+02:00",
        "type": "maintenance",
        "address": "Urbanstraße 76, 10967 Berlin",
        "siteprofile_uuid": "5fa79e8b-599c-4a70-97ef-989f0c823e5d",
        "invitee_uuids": ["44852b4a-4e80-448e-8936-71c4c294a1b7"],
        "workflowlevel2_uuids": ["7b504be7-36e3-4196-8c60-227b78f8ae96"],
        "contact_uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "summary": "",
    }, # Lilly with billing
    {
        "uuid": "9ba34824-a224-4da9-8ace-e24a1006c231",
        "id": "9ba34824-a224-4da9-8ace-e24a1006c231",
        "notes": [
            {"id": 1979, "note": "Bitte Standardwartung durchführen", "type": 1},
            {"id": 1980, "note": "", "type": 3},
        ],
        "name": "Kupfer Appointment",
        "start_date": f"{Thursday}T10:25:00+02:00",
        "end_date": f"{Thursday}T13:25:00+02:00",
        "type": "maintenance",
        "address": "Lehmbruckstraße 12, 10245 Berlin",
        "siteprofile_uuid": "485234bd-1bd6-49b9-81b9-7d84161b6b39",
        "invitee_uuids": ["44852b4a-4e80-448e-8936-71c4c294a1b7"],
        "workflowlevel2_uuids": ["999d0b08-759f-49d6-b121-e312c3ea17c5"],
        "contact_uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "summary": "",
    }, # Ema with object
    {
        "uuid": "951609b6-32e9-43e6-8f24-692462a81496",
        "id": "951609b6-32e9-43e6-8f24-692462a81496",
        "notes": [
            {"id": 1981, "note": "", "type": 1},
            {"id": 1982, "note": "", "type": 3},
        ],
        "name": "Kupfer Appointment",
        "start_date": f"{Thursday}T19:25:00+02:00",
        "end_date": f"{Thursday}T21:25:00+02:00",
        "type": "installation",
        "address": "Friedrichstraße 233, 10969 Berlin",
        "siteprofile_uuid": "900498a7-8630-4c7c-9762-2447cc2178ce",
        "invitee_uuids": [
            "44852b4a-4e80-448e-8936-71c4c294a1b7",
            "3418abb1-faff-4f38-86d9-606f3f542ef5",
            "40517e88-26cb-4b34-853f-ed383c1af0d6",
        ],
        "workflowlevel2_uuids": ["8132d789-9580-45ad-b22a-9384bce0eed6"],
        "contact_uuid": "61a012e5-d70b-4801-acb3-507b913fcd54",
        "summary": "",
    }, # Kutay with object
    {
        "uuid": "ae4bde84-7f02-436f-b666-70d032ee8d61",
        "id": "ae4bde84-7f02-436f-b666-70d032ee8d61",
        "notes": [
            {"id": 1984, "note": "", "type": 3},
            {"id": 1983, "note": "Bitte Ventile prüfen und austauschen.", "type": 1},
        ],
        "name": "Kupfer Appointment",
        "start_date": f"{Friday}T10:00:00+02:00",
        "end_date": f"{Friday}T11:50:00+02:00",
        "type": "repair",
        "address": "Tempelhofer Ufer 13, 10963 Berlin",
        "siteprofile_uuid": "551629e8-bb28-4734-a3e4-7edb239854b2",
        "invitee_uuids": [
            "44852b4a-4e80-448e-8936-71c4c294a1b7",
            "3418abb1-faff-4f38-86d9-606f3f542ef5",
            "40517e88-26cb-4b34-853f-ed383c1af0d6",
        ],
        "workflowlevel2_uuids": ["9e3bda19-49e5-428a-a2cc-ef03153f14bb"],
        "contact_uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "summary": "",
    }, # Franziska with object
    {
        "uuid": "0be0eda0-bcd1-4126-84c3-96975250025c",
        "id": "0be0eda0-bcd1-4126-84c3-96975250025c",
        "contact": None,
        "notes": [
            {
                "id": 3220,
                "note": "",
                "type": 1
            },
            {
                "id": 3221,
                "note": "",
                "type": 3
            }
        ],
        "driving_times": [],
        "name": "Abwesend",
        "start_date": f"{Wednesday}T11:40:00+02:00",
        "end_date": f"{Wednesday}T13:40:00+02:00",
        "type": "out-of-office",
        "address": "Abwesend",
        "siteprofile_uuid": None,
        "invitee_uuids": [],
        "workflowlevel2_uuids": [],
        "contact_uuid": None,
        "summary": "",
        "location": None
    },
    {
        "uuid": "62e90b81-00f1-4d1c-b12e-7df0edceaab7",
        "id": "62e90b81-00f1-4d1c-b12e-7df0edceaab7",
        "contact": None,
        "notes": [
            {
                "id": 3222,
                "note": "",
                "type": 1
            },
            {
                "id": 3223,
                "note": "",
                "type": 3
            }
        ],
        "driving_times": [],
        "name": "Abwesend",
        "start_date": f"{Monday}T08:40:00+02:00",
        "end_date": f"{Monday}T11:40:00+02:00",
        "type": "out-of-office",
        "address": "Abwesend",
        "siteprofile_uuid": None,
        "invitee_uuids": [
            "acca56ea-e088-4cd8-bcfa-80545bab2f95" # !!!!!!!!!
        ],
        "workflowlevel2_uuids": [],
        "contact_uuid": None,
        "summary": "",
        "location": None
    },
]


# Product Service

product_categories = [
    {
        "uuid": "75207588-9956-4331-af63-4b0307ac09aa",
        "id": "75207588-9956-4331-af63-4b0307ac09aa",
        "name": "HEATING_SYSTEM",
        "is_global": True,
        "parent": None,
    },
    {
        "uuid": "6989cbe9-307f-49f2-b841-f40c74acf840",
        "id": "6989cbe9-307f-49f2-b841-f40c74acf840",
        "name": "GAS_CONDENSING",
        "is_global": True,
        "level": 1,
        "parent": "75207588-9956-4331-af63-4b0307ac09aa",
    },
]

products = [
    {
        "id": "58e599ca-e6e7-48bd-9ca1-29e988ce7a74",
        "category_display": "HEATING_SYSTEM",
        "subcategory_display": "GAS_CONDENSING",
        "part_number": "",
        "installation_date": "2019-07-02",
        "recurring_check_interval": "12",
        "notes": "",
        "workflowlevel2_uuid": "999d0b08-759f-49d6-b121-e312c3ea17c5",
        "name": "Vitodens 200",
        "make": "Viessmann",
        "type": "",
        "reference_id": "9049384729385732",
        "organization_uuid": "a7d7f137-94e4-4fa9-8ac1-3456a1611a71",
        "category": "6989cbe9-307f-49f2-b841-f40c74acf840",
    },
    {
        "id": "9f20afc3-bd55-4d28-b163-a6b810963a4e",
        "category_display": "HEATING_SYSTEM",
        "subcategory_display": "GAS_CONDENSING",
        "part_number": "",
        "installation_date": "2019-07-30",
        "recurring_check_interval": "12",
        "notes": "",
        "workflowlevel2_uuid": "8132d789-9580-45ad-b22a-9384bce0eed6",
        "name": "Vitodens 200",
        "make": "Viessmann",
        "type": "",
        "reference_id": "9049384729385732",
        "organization_uuid": "a7d7f137-94e4-4fa9-8ac1-3456a1611a71",
        "category": "6989cbe9-307f-49f2-b841-f40c74acf840",
    },
]


# TimeTracking Service

time_events = [
    {
        "id": "ff294372-0e58-4e6c-8ea9-20b9b7d9b8c5",
        "core_user_uuid": "44852b4a-4e80-448e-8936-71c4c294a1b7",
        "workflowlevel1_uuid": None,
        "workflowlevel2_uuid": "8132d789-9580-45ad-b22a-9384bce0eed6",
        "appointment_uuid": "432aa435-f9ec-4984-87d3-31f1b2a9388e",
    },
    {
        "id": "a1976b92-2337-415b-ae7e-9e907d1e46ef",
        "core_user_uuid": None,
        "workflowlevel1_uuid": None,
        "workflowlevel2_uuid": "8132d789-9580-45ad-b22a-9384bce0eed6",
        "appointment_uuid": "951609b6-32e9-43e6-8f24-692462a81496",
    },
    {
        "id": "1ec0afa2-4b3d-4fb6-9bcb-8a74cd959d86",
        "core_user_uuid": "44852b4a-4e80-448e-8936-71c4c294a1b7",
        "workflowlevel1_uuid": None,
        "workflowlevel2_uuid": "6f015067-db3e-40be-8f87-8b20fa347752",
        "appointment_uuid": "878db099-b8c1-4482-b4a8-11e26168c933",
    },
    {
        "id": "e53f6ba2-9c46-4570-b57c-9bbb89d9c745",
        "core_user_uuid": "44852b4a-4e80-448e-8936-71c4c294a1b7",
        "workflowlevel1_uuid": None,
        "workflowlevel2_uuid": "9e3bda19-49e5-428a-a2cc-ef03153f14bb",
        "appointment_uuid": "edeb1722-5b43-4eb0-ae52-b5598e40e704",
    },
    {
        "id": "5a4dd781-3a71-4940-84ce-265167793780",
        "core_user_uuid": "44852b4a-4e80-448e-8936-71c4c294a1b7",
        "workflowlevel1_uuid": None,
        "workflowlevel2_uuid": "9e3bda19-49e5-428a-a2cc-ef03153f14bb",
        "appointment_uuid": "ae4bde84-7f02-436f-b666-70d032ee8d61",
    },
    {
        "id": "2e3dfb85-e732-4415-b8d9-d07e779709de",
        "core_user_uuid": "44852b4a-4e80-448e-8936-71c4c294a1b7",
        "workflowlevel1_uuid": None,
        "workflowlevel2_uuid": "9e3bda19-49e5-428a-a2cc-ef03153f14bb",
        "appointment_uuid": "138b1db2-322d-4f4f-bd04-a81737adc15e",
    },
    {
        "id": "cc7bab28-d0cc-40fa-a3f9-23c572ec723e",
        "core_user_uuid": "44852b4a-4e80-448e-8936-71c4c294a1b7",
        "workflowlevel1_uuid": None,
        "workflowlevel2_uuid": "9e3bda19-49e5-428a-a2cc-ef03153f14bb",
        "appointment_uuid": "bcc6c746-faab-489d-9d37-eb7d431e4e9d",
    },
    {
        "id": "aa236c72-dfbd-436b-98e4-704bd3da6142",
        "core_user_uuid": None,
        "workflowlevel1_uuid": None,
        "workflowlevel2_uuid": "7b504be7-36e3-4196-8c60-227b78f8ae96",
        "appointment_uuid": "ed4c7e5a-5211-486e-a0ca-fcde746a8e2e",
    },
    {
        "id": "09539017-2be1-48fe-b5a5-1c85c4f63d08",
        "core_user_uuid": "44852b4a-4e80-448e-8936-71c4c294a1b7",
        "workflowlevel1_uuid": None,
        "workflowlevel2_uuid": "999d0b08-759f-49d6-b121-e312c3ea17c5",
        "appointment_uuid": "9ba34824-a224-4da9-8ace-e24a1006c231",
    }
]

time_log_entries = []


# Documents Service

documents = [
    {
        "id": 22849,
        "file_description": "undefined",
        "file_name": "Pic_1.jpg",
        "file_type": "jpg",
        "organization_uuid": None,
        "create_date": "2019-07-30T13:36:05.311000Z",
        "workflowlevel2_uuids": ["8132d789-9580-45ad-b22a-9384bce0eed6"],
    },
    {
        "id": 22850,
        "file_description": "undefined",
        "file_name": "Pic_2.png",
        "file_type": "png",
        "organization_uuid": None,
        "create_date": "2019-07-30T13:36:05.311000Z",
        "workflowlevel2_uuids": ["8132d789-9580-45ad-b22a-9384bce0eed6"],
    },
    {
        "id": 22851,
        "file_description": "undefined",
        "file_name": "Pic_3.jpg",
        "file_type": "jpg",
        "organization_uuid": None,
        "create_date": "2019-07-30T13:36:05.311000Z",
        "workflowlevel2_uuids": ["8132d789-9580-45ad-b22a-9384bce0eed6"],
    },
    {
        "id": 22852,
        "file_description": "undefined",
        "file_name": "Datenblatt_Vitodens.pdf",
        "file_type": "pdf",
        "organization_uuid": None,
        "create_date": "2019-07-30T13:36:05.311000Z",
        "workflowlevel2_uuids": ["8132d789-9580-45ad-b22a-9384bce0eed6"],
    },
    {
        "id": 22853,
        "file_description": "undefined",
        "file_name": "Pic_1.jpg",
        "file_type": "jpg",
        "organization_uuid": None,
        "create_date": "2019-07-30T13:36:05.311000Z",
        "workflowlevel2_uuids": ["999d0b08-759f-49d6-b121-e312c3ea17c5"],
    },
    {
        "id": 22854,
        "file_description": "undefined",
        "file_name": "Pic_3.jpg",
        "file_type": "jpg",
        "organization_uuid": None,
        "create_date": "2019-07-30T13:36:05.311000Z",
        "workflowlevel2_uuids": ["999d0b08-759f-49d6-b121-e312c3ea17c5"],
    },
    {
        "id": 22855,
        "file_description": "undefined",
        "file_name": "Pic_2.png",
        "file_type": "png",
        "organization_uuid": None,
        "create_date": "2019-07-30T13:36:05.311000Z",
        "workflowlevel2_uuids": ["999d0b08-759f-49d6-b121-e312c3ea17c5"],
    },
    {
        "id": 22856,
        "file_description": "undefined",
        "file_name": "Datenblatt_Vitodens.pdf",
        "file_type": "pdf",
        "organization_uuid": None,
        "create_date": "2019-07-30T13:36:05.311000Z",
        "workflowlevel2_uuids": ["999d0b08-759f-49d6-b121-e312c3ea17c5"],
    },
]

SEED_DATA = {
    "extensions": {
        "projectextensions": {
            "data": projectextensions,
            "update_fields": {"workflowlevel2_uuid": "workflowlevel2"},
        }
    },
    "location": {
        # 'profiletypes': {
        #     'data': profiletypes,
        # },
        "siteprofiles": {
            "data": siteprofiles,
            "update_fields": {
                "workflowlevel2_uuid": "workflowlevel2",
                "profiletype": "profiletypes",
            },
        }
    },
    "crm": {
        "contact": {
            "data": contacts,
            "update_fields": {
                "siteprofile_uuids": "siteprofiles",
                "workflowlevel1_uuids": "workflowlevel1",
                "workflowlevel2_uuids": "workflowlevel2",
            },
        },
        "appointment": {
            "data": appointments,
            "update_fields": {
                "contact_uuid": "contact",
                "siteprofile_uuid": "siteprofiles",
                "workflowlevel2_uuids": "workflowlevel2",
            },
            "update_dates": {
                "start_date": "week_of_the_org_created_week",
                "end_date": "week_of_the_org_created_week",
            },
            "set_fields": {
                "invitee_uuids": "org_core_user_uuids",
            },
        }
    },
    "products": {
        # 'categories?is_global=true': {
        #     'data': product_categories,
        # },
        "products": {
            "data": products,
            "update_fields": {
                "category": "categories",
                "workflowlevel2_uuid": "workflowlevel2",
            },
        },
    },
    "timetracking": {
        "time-event": {
            "validate": False,
            "data": time_events,
            "update_fields": {
                "workflowlevel2_uuid": "workflowlevel2",
                "appointment_uuid": "appointment",
            },
        },
        "time-log-entry": {
            "validate": False,
            "data": time_log_entries,
            "update_fields": {
                "time_event": "time-event",
            },
            "update_dates": {
                "start_time": 0,
                "end_time": {
                    "hours": 1,
                    "minutes": 25,
                },
            },
        },
    },
    "documents": {
        "documents": {
            "validate": False,
            "data": documents,
            "update_fields": {
                "workflowlevel2_uuids": "workflowlevel2",
            },
            "upload_files": {
                "file_name": "workflow/seeds/files/",
            },
            "set_fields": {
                "organization_uuid": "organization_uuid",
            },
            "update_dates": {
                "create_date": 0,
            },
        },
    },
}


# Bifrost Data

workflowleveltypes = [
    {"uuid": "e2bafb25-c6ee-45c1-93bf-82e3206f8f29", "name": "INSTALLATION"},
    {"uuid": "c17709b0-3acf-4a93-9d14-a5a5f59fcb77", "name": "MAINTENANCE"},
    {"uuid": "ad4937f3-0282-4d66-ac8c-4d9b903ee1cd", "name": "REPAIR"},
    {"uuid": "eb6fd665-af47-429d-aad4-8cf6622f656b", "name": "REPLACEMENT"},
    {"uuid": "9af16012-9f8a-40ce-827e-4ed6be711677", "name": "EMERGENCY"},
    {"uuid": "b0b81450-db28-4d1b-b036-9cf5c36db4be", "name": "OTHERS"},
]

workflowlevel2s = [
    {
        "level2_uuid": "8132d789-9580-45ad-b22a-9384bce0eed6",
        "description": "Bitte neuen Kessel einbauen.",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "end_date": "2019-08-22T00:00:00+02:00",
        "workflowlevel1": 18,
        "type": "e2bafb25-c6ee-45c1-93bf-82e3206f8f29",
    },
    {
        "level2_uuid": "999d0b08-759f-49d6-b121-e312c3ea17c5",
        "description": "Neuinstallation Vitodens 200",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "workflowlevel1": 18,
        "type": "e2bafb25-c6ee-45c1-93bf-82e3206f8f29",
    },
    {
        "level2_uuid": "6f015067-db3e-40be-8f87-8b20fa347752",
        "description": "Bitte Standardwartung durchführen",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "workflowlevel1": 18,
        "type": "c17709b0-3acf-4a93-9d14-a5a5f59fcb77",
    },
    {
        "level2_uuid": "7b504be7-36e3-4196-8c60-227b78f8ae96",
        "description": "Bitte Standardwartung durchführen",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "workflowlevel1": 18,
        "type": "c17709b0-3acf-4a93-9d14-a5a5f59fcb77",
    },
    {
        "level2_uuid": "37c40d1b-fe9b-4174-86aa-b77adbb739a8",
        "description": "Bitte Standardwartung durchführen",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "workflowlevel1": 18,
        "type": "c17709b0-3acf-4a93-9d14-a5a5f59fcb77",
    },
    {
        "level2_uuid": "fd98dce0-24f9-4f42-a0f7-febeff3b1174",
        "description": "Bitte Standardwartung durchführen",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "workflowlevel1": 18,
        "type": "c17709b0-3acf-4a93-9d14-a5a5f59fcb77",
    },
    {
        "level2_uuid": "9e3bda19-49e5-428a-a2cc-ef03153f14bb",
        "description": "Bitte Standardwartung durchführen",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "workflowlevel1": 18,
        "type": "c17709b0-3acf-4a93-9d14-a5a5f59fcb77",
    },
    {
        "level2_uuid": "a12e9ec2-e9cd-45e0-849c-ddbc74293bc9",
        "description": "Bitte Standardwartung durchführen",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "workflowlevel1": 18,
        "type": "c17709b0-3acf-4a93-9d14-a5a5f59fcb77",
    },
    {
        "level2_uuid": "3a63d21a-c111-405b-beaf-a3a0920bc9ac",
        "description": "Bitte Standardwartung durchführen",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "workflowlevel1": 18,
        "type": "c17709b0-3acf-4a93-9d14-a5a5f59fcb77",
    },
    {
        "level2_uuid": "6ecf272c-b574-404e-a4eb-e9b9955c72ce",
        "description": "Bitte Standardwartung durchführen",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "workflowlevel1": 18,
        "type": "c17709b0-3acf-4a93-9d14-a5a5f59fcb77",
    },
    {
        "level2_uuid": "5aa823a9-d3c6-4c6d-92fa-ec1e92c5ee3d",
        "description": "Bitte Standardwartung durchführen",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "workflowlevel1": 18,
        "type": "c17709b0-3acf-4a93-9d14-a5a5f59fcb77",
    },
    {
        "level2_uuid": "f0ad19c1-a09b-4e05-a96c-804d6ef3efa8",
        "description": "Bitte Standardwartung durchführen",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "workflowlevel1": 18,
        "type": "c17709b0-3acf-4a93-9d14-a5a5f59fcb77",
    },
    {
        "level2_uuid": "af4c9679-5b2c-4f75-8014-f384bca3c5ef",
        "description": "Bitte Standardwartung durchführen",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "workflowlevel1": 18,
        "type": "c17709b0-3acf-4a93-9d14-a5a5f59fcb77",
    },
    {
        "level2_uuid": "7ac41a5c-0a4c-4fff-a1c7-92dc25bc7dba",
        "description": "Bitte Standardwartung durchführen",
        "name": "New Kupfer Project",
        "parent_workflowlevel2": 0,
        "workflowlevel1": 18,
        "type": "c17709b0-3acf-4a93-9d14-a5a5f59fcb77",
    },
]


# Datamesh Data

join_records = [
    {
        "record_uuid": "61a012e5-d70b-4801-acb3-507b913fcd54",
        "related_record_uuid": "900498a7-8630-4c7c-9762-2447cc2178ce",
        "origin_model_name": "crmContact",
        "related_model_name": "locationSiteProfile",
    },
    {
        "record_uuid": "a73ae6b9-66b2-4ae4-9f2c-d1765eb42869",
        "related_record_uuid": "551629e8-bb28-4734-a3e4-7edb239854b2",
        "origin_model_name": "crmContact",
        "related_model_name": "locationSiteProfile",
    },
]
