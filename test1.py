from fhirclient import client
settings = {
    'app_id': '823a2a87-293b-4824-be2a-493b9d7330bc',
    'api_base': 'https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4',
    # 'api_base': "https://open-ic.epic.com/Argonaut/api/FHIR/Argonaut",
}
smart = client.FHIRClient(settings=settings)
smart.prepare()
print(smart.ready)
# import fhirclient.models.patient as p
# patient = p.Patient.read('hca-pat-1', smart.server)
# print(patient)
# patient.birthDate.isostring
# # '1963-06-12'
# smart.human_name(patient.name[0])