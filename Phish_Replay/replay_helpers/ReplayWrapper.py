# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
import json
import os

def RunActions(action_runner):
  with open(os.path.join(os.path.dirname(__file__), os.path.pardir, 'data','RecordedData.json')) as f:
    data = json.load(f)
  url= data["url"]
  action_runner.Navigate(url)
  action_runner.WaitForJavaScriptCondition(
        'document.readyState == "complete"')
  
  for pages in data["pages"]:
    action_runner.WaitForJavaScriptCondition(
        'document.readyState == "complete"')
    frmId=pages["formId"];
    for values in pages["values"]:
      if values["tag"] =="INPUT":
        if values["type"] in ["radio","checkbox"]:
	  CheckForm(action_runner, values["value"], values["name"],None)
        else:
          InputForm(action_runner, values["value"], values["name"],None)
      elif values["tag"]=="SELECT":
        SelectForm(action_runner, values["value"], values["name"],None)
    action_runner.Wait(4)
    if frmId !="":
      action_runner.ExecuteJavaScript('''
        
          document.forms["%s"].submit();''' %(frmId))
    else:
      action_runner.ExecuteJavaScript('''
        
          document.forms[0].submit();''' )


def InputForm(action_runner, input_text, input_name, form_id=None):
 
  if form_id and input_name:
    element_selector = '#%s input[name=\"%s\"]' % (form_id, input_name)
  elif input_name:
    element_selector = 'input[name=\"%s\"]' % (input_name)
  else:
    raise ValueError("Input ID can not be None or empty.")
  action_runner.WaitForElement(selector=element_selector)
  action_runner.ExecuteJavaScript(
      'document.querySelector(\'%s\').value = "%s";' %
      (element_selector, input_text))

def SelectForm(action_runner, input_text, input_name, form_id=None):
 
  if form_id and input_name:
    element_selector = '#%s select[name=\"%s\"]' % (form_id, input_name)
  elif input_name:
    element_selector = 'select[name=\"%s\"]' % (input_name)
  else:
    raise ValueError("Input ID can not be None or empty.")
  action_runner.WaitForElement(selector=element_selector)
  action_runner.ExecuteJavaScript(
      'document.querySelector(\'%s  [value="%s"]\').selected = true;' %
      (element_selector, input_text))

def CheckForm(action_runner, input_text, input_name, form_id=None):
 
  if form_id and input_name:
    element_selector = '#%s input[name=\"%s\"]' % (form_id, input_name)
  elif input_name:
    element_selector = 'input[name=\"%s\"]' % (input_name)
  else:
    raise ValueError("Input ID can not be None or empty.")
  action_runner.WaitForElement(selector=element_selector)
  action_runner.ExecuteJavaScript(
      'document.querySelector(\'%s[value="%s"]\').checked = true;' %
      (element_selector, input_text))
