'''
Created on Sep 20, 2019

@author: SGeary
'''

import logging

import config
import FNCI.v7.tasks.getTasks


logger = logging.getLogger(__name__)


authToken = config.AUTHTOKEN
#------------------------------------------------------------------#

def get_v7_task_data(projectID):
    
    logger.debug("Entering get_v7_task_data with projectID: %s" %projectID)
    
    # Empty dict to hold the inventory item id and task id
    PROJECTTASKS = {}
    
    # Get the task data
    TASKS = FNCI.v7.tasks.getTasks.get_task_by_projectID(projectID, authToken)
    
    if len(TASKS) > 0:
        # Cycle through the associated tasks for the project
        for task in TASKS:
            inventoryId = task["inventoryId"]
            workflowTaskType = task["workflowTaskType"]
    
            
            # We only care about task of type MANUAL_INVENTORY_REVIEWw
            if workflowTaskType == "MANUAL_INVENTORY_REVIEW":
                taskId = task["id"]
             
                PROJECTTASKS[taskId] = inventoryId

        return PROJECTTASKS