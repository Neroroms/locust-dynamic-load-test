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
    testFileVariable = loadTestData[2]

    if len(testFileVariable) > 0:
      with open(path.join(loadTestFilePath,testFileVariable)) as jsonFile:
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

#Setup locust task
locustTaskList = {}

for loadTestSetup in loadTestSetups:
  locustTaskList[locustFactory(loadTestSetup)] = 1

class loadTestTasks(TaskSet):
  tasks = locustTaskList

class loadTest(HttpLocust):
  wait_time = constant(waitTimePerRequest)
  task_set = loadTestTasks
