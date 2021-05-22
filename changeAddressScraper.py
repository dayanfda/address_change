# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:02:31 2021

@author: dayan
"""

import os
import time
import csv
import shutil
import random 
import urllib
import unittest
import pandas as pd
from datetime import datetime
from selenium import webdriver
from time import gmtime, strftime
from collections import OrderedDict
from urllib.request import urlretrieve
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setUp():
    
    global driver
    try:
        driver.quit()
    except:
        pass
        driver = webdriver.Chrome()
    driver.get('https://changemailaddress.com/wp-login.php?redirect_to=https%3A%2F%2Fchangemailaddress.com%2Fwp-admin%2Fadmin.php%3Fpage%3Dusps-listing&reauth=1')
    
    driver.execute_script("window.open('');")
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://changemailaddress.com/')
    driver.switch_to.window(driver.window_handles[0])

#===============================================================================
#===============================================================================
# LOG IN
    
    
def enterUserName():
    username = driver.find_element_by_xpath("//input[@id='user_login']")
    username.send_keys("daniel")
    time.sleep(1)
    print('username entered')
    

def enterPassword():
    password = driver.find_element_by_xpath("//input[@id='user_pass']")
    password.send_keys("Change8989USPS")
    time.sleep(1)
    print('password entered')

def clickSubmit():
    driver.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(1)
    
#Control-------------------------
def logIn():
    enterUserName()
    enterPassword()
    clickSubmit()

        
# #===============================================================================
# #===============================================================================


def clickEye():
    driver.find_element_by_xpath('//i[@class="fas fa-eye"]').click()
    time.sleep(1)


# #===============================================================================
# #===============================================================================


def parseWho():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    who = tableInfo.split("Who's Moving: ")[1].split('\n')[0]
    print("person moving - "+str(who))
    return who


def parseTypeMove():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    typeMove = tableInfo.split("Type of Move: ")[1].split('\n')[0]
    print("type of move - "+str(typeMove))
    return typeMove
    
def parseForwardingDate():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    forwardingDate = tableInfo.split("Forwarding Date: ")[1].split('\n')[0]
    print("forwarding date - "+str(forwardingDate))
    return forwardingDate
    
def parseFirstName():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    firstName = tableInfo.split("First Name: ")[1].split('\n')[0]
    print("first name - "+str(firstName))
    return firstName
    
def parseMiddleName():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    middleName = tableInfo.split("Middle Name or Initial: ")[1].split('\n')[0]
    print("middle name - "+str(middleName))
    return middleName
    
def parseLastName():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    lastName = tableInfo.split("Last Name: ")[1].split('\n')[0]
    print("last name - "+str(lastName))
    return lastName
    
def parseSuffix():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    suffix = tableInfo.split("Suffix: ")[1].split('\n')[0]
    print("suffix - "+str(suffix))
    return suffix

def parseEmail():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    email = tableInfo.split("Email Address: ")[1].split('\n')[0]
    print("email - "+str(email))
    return email
    
def parsePhoneNumber():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    phoneNumber = tableInfo.split("Phone Number: ")[1].split('\n')[0]
    print("phone number - "+str(phoneNumber))
    return phoneNumber
    
def parsePhoneType():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    phoneType = tableInfo.split("Phone Type: ")[1].split('\n')[0]
    print("phone type - "+str(phoneType))
    return phoneType
  
    # OLD ADDRESS
def parse_oldZIPCode():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    oldZIPCode = tableInfo.split("ZIP Code: ")[1].split('\n')[0]
    print("previous zip code - "+str(oldZIPCode))
    return oldZIPCode
    
def parse_oldCity():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    oldCity = tableInfo.split("City: ")[1].split('\n')[0]
    print("previous city - "+str(oldCity))
    return oldCity
    
def parse_oldState():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    oldState = tableInfo.split("State: ")[1].split('\n')[0]
    print("previous state - "+str(oldState))
    return oldState
    
def parse_oldStreetAddress():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    oldStreetAddress = tableInfo.split("Street Address: ")[1].split('\n')[0]
    print("previous street address - "+str(oldStreetAddress))
    return oldStreetAddress
    
    # NEW ADDRESS
def parse_newZIPCode():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    newZIPCode = tableInfo.split("ZIP Code: ")[2].split('\n')[0]
    print("new zip code - "+str(newZIPCode))
    return newZIPCode
    
def parse_newCity():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    newCity = tableInfo.split("City: ")[2].split('\n')[0]
    print("new city - "+str(newCity))
    return newCity
    
def parse_newState():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    newState = tableInfo.split("State: ")[2].split('\n')[0]
    print("new state - "+str(newState))
    return newState

def parse_newStreetAddress():
    tableInfo = driver.find_element_by_xpath('//table[@class="table table-bordered user_details"]').text
    newStreetAddress = tableInfo.split("Street Address: ")[2].split('\n')[0]
    print("new street address - "+str(newStreetAddress))
    return newStreetAddress
    


def parseList():
    global personInfo 
    who = parseWho()
    typeMove = parseTypeMove()
    forwardingDate = parseForwardingDate()
    firstName = parseFirstName()
    middleName = parseMiddleName()
    lastName = parseLastName()
    suffix = parseSuffix()
    email = parseEmail()
    phoneNumber = parsePhoneNumber()
    phoneType = parsePhoneType()
    oldZIPCode = parse_oldZIPCode()
    oldCity = parse_oldCity()
    oldState = parse_oldState()
    oldStreetAddress = parse_oldStreetAddress()
    newZIPCode = parse_newZIPCode()
    newCity = parse_newCity()
    newState = parse_newState()
    newStreetAddress = parse_newStreetAddress()
    
    personInfo = [who, typeMove, forwardingDate, firstName, middleName, lastName, suffix, email, phoneNumber, phoneType, oldZIPCode, oldCity, oldState, oldStreetAddress, newZIPCode, newCity, newState, newStreetAddress]
    return personInfo
    



# def parse():
 
def goToPreviousPage():
    driver.back()  
   # driver.execute_script("window.history.go(-1)")
    
    


# #Control-------------------------
# currentRow = []
# def parse():
#     currentList.append(parseWho())
#     currentList.append(parseTypeMove())
#     currentList.append(ParseForwardingDate())
#     currentList.append(parseMiddleName())
#     #Finish the rest of the function you have
#     return currentRow
# #===============================================================================
# #===============================================================================

# dataList=[]
def start():
    for i in range(len(totalOrders)):
        setUp()
        logIn()
        clickEye()
        parseList()
        goToLastPage()
#     orders = #total amount of eyes buttons on the page
#     num = len(eyes)
    
        
# #===============================================================================
# #===============================================================================
# #OPTIONAL
# #def save():# use what you use last time to save the row into CSV
# #    











