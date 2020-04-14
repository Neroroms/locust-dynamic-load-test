from locust import HttpLocust, TaskSet, constant
from support_function import *

import csv, os, json

scriptPath = os.path.abspath(os.path.dirname(__file__))
waitTimePerRequest = 2

loadTestFilePath = ""
loadTestFileInfoName = ""

with open(path.join(scriptPath, "config.json")) as jsonFile:
  configJson = json.load(jsonFile)

  loadTestFilePath = path.join(scriptPath, configJson['loadTestFile']['path'])
  loadTestFileInfoName = configJson['loadTestFile']['infoName'] + ".csv"

  if path.exists(path.join(loadTestFilePath, loadTestFileInfoName)) == False:
    print("Load test file not found.")
    exit(1)

  if len(configJson['waitTimePerRequest']) > 0:
    waitTimePerRequest = int(configJson['waitTimePerRequest'])
  else:
    waitTimePerRequest = 2  

#Setup load test information
loadTestSetups = []

with open(path.join(loadTestFilePath, loadTestFileInfoName)) as loadTestCsv:
  loadTestDatas = csv.reader(loadTestCsv)

  for loadTestData in loadTestDatas:
    loadTestMethodType = loadTestData[0]
    loadTestUrl = loadTestData[1]
    loadTestVariableFileName = loadTestData[2]
    loadTestExpectStatusCode = loadTestData[3]

    loadTestSetup = {}

    if len(loadTestVariableFileName) > 0:
      with open(path.join(loadTestFilePath,loadTestVariableFileName)) as jsonFile:
        pathVariables = json.load(jsonFile)

        for pathVariable in pathVariables['data']:
          loadTestSetups.append(
            createLoadTestObject(
              url = replaceVariable(loadTestUrl, pathVariable),
              methodType = loadTestMethodType,
              expectStatusCode = loadTestExpectStatusCode
            )
          )
    else:
      loadTestSetups.append(
        createLoadTestObject(
          url = loadTestUrl,
          methodType = loadTestMethodType,
          expectStatusCode = loadTestExpectStatusCode
        )
      )

#Setup locust task
locustTaskList = {}

for loadTestSetup in loadTestSetups:
  locustTaskList[locustFactory(loadTestSetup)] = 1

class loadTestTasks(TaskSet):
  tasks = locustTaskList

class loadTest(HttpLocust):
  wait_time = constant(waitTimePerRequest)
  task_set = loadTestTasks
