import pytest
import requests
import jsonschema
from pytest_bdd import scenarios, when, then, parsers

scenarios('../features/api/countries.feature')

@pytest.fixture
def context():
    return {}

@when(parsers.parse('I request countries with currency "{currency}"'))
def request_countries(context, currency):
    context['response'] = requests.get(
        f"https://restcountries.com/v3.1/currency/{currency}"
    )

@then(parsers.parse('the response status code should be {status_code:d}'))
def verify_status_code(context, status_code):
    assert context['response'].status_code == status_code

@then("the response should contain at least one country")
def verify_country_present(context):
    data = context['response'].json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "name" in data[0]

@then(parsers.parse('the response should contain message "{message}"'))
def verify_error_message(context, message):
    data = context['response'].json()
    assert data["message"] == message

@then("the response should match the expected schema")
def verify_schema(context):
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "name": {"type": "object"},
                "currencies": {"type": "object"},
                "capital": {"type": "array"},
                "region": {"type": "string"},
                "languages": {"type": "object"},
                "borders": {"type": "array"},
                "population": {"type": "number"}
            },
            "required": ["name", "currencies", "capital", "region"]
        }
    }
    jsonschema.validate(instance=context['response'].json(), schema=schema)