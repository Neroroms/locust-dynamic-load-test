from locust import HttpLocust, TaskSet, task, constant
from support_function import *

import csv, os, json

scriptPath = os.path.abspath(os.path.dirname(__file__))
loadTestCsvFileName = "loadTestInfo.csv"

def checkCsvFileConvention(csvRow):
  #Check load test path
  checkStringOk(csvRow[0])

  #Check method type
  checkStringOk(csvRow[1])

  #Check variable file exists
  if csvRow[2].strip().len() > 0:
    checkFileExist(csvRow[2])

#Setup load test information
loadTestSetups = []

with open(path.join(scriptPath, loadTestCsvFileName)) as loadTestCsv:
  loadTestDatas = csv.reader(loadTestCsv)

  for loadTestData in loadTestDatas:
    testFileVariable = loadTestData[2]

    if testFileVariable.len() > 0:
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
