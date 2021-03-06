import pytest

@pytest.mark.usefixtures('class_fixture')
@pytest.mark.usefixtures('setUp')
@pytest.mark.usefixtures('data')
class TestDemo:

	def test_getDataFromFrom_conftest(self, data):
		print('class test method3 execution')
		print(data[0])
		print(data[1])
		print(data[2])

	@pytest.mark.usefixtures('data_provider')
	def test_parameterization_fromConftest(self, data_provider):
		print('Class test method4 execution')
		print(data_provider['user'])
		print(data_provider['pass'])

#  pytest -v -s test_09_get_data_parameterization.py