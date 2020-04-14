from locust import HttpLocust, TaskSet, constant
from support_function import *

import csv, os, json

scriptPath = os.path.abspath(os.path.dirname(__file__))
loadTestCsvFileName = "loadTestInfo.csv"

#Setup load test information
loadTestSetups = []

with open(path.join(scriptPath, loadTestCsvFileName)) as loadTestCsv:
  loadTestDatas = csv.reader(loadTestCsv)

  for loadTestData in loadTestDatas:
    testFileVariable = loadTestData[2]

    if len(testFileVariable) > 0:
      with open(path.join(scriptPath, testFileVariable)) as jsonFile:
        pathVariables = json.load(jsonFile)

        for pathVariable in pathVariables['data']:
          loadTestSetups.append(
            {
              "url": replaceVariable(loadTestData[0], pathVariable),
              "methodType": loadTestData[1]
            }
          )
    else:
      loadTestSetups.append(
        {
          "url": loadTestData[0],
          "methodType": loadTestData[1]
        }
      )

print(loadTestSetups)

#Setup locust task
locustTaskList = {}

for loadTestSetup in loadTestSetups:
  locustTaskList[locustFactory(loadTestSetup)] = 1

class loadTestTasks(TaskSet):
  tasks = locustTaskList

class loadTest(HttpLocust):
  wait_time = constant(2)
  task_set = loadTestTasks
