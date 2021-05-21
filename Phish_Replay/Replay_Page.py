# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
from telemetry.page import page as page_module
from telemetry import story
from page_sets.startup_pages import BrowserStartupSharedState
from page_sets.replay_helpers import ReplayWrapper

class ReplayPage(page_module.Page):
  def __init__(self, url, page_set):
    super(ReplayPage, self).__init__(url, page_set=page_set)
    self.archive_data_file = 'data/blank_page.json'

  def RunPageInteractions(self, action_runner):
    # Request a RAF and wait for it to be processed to ensure that the metric
    # Startup.FirstWebContents.NonEmptyPaint2 is recorded.
    action_runner.ExecuteJavaScript(
        """
        this.hasRunRAF = 0;
        requestAnimationFrame(function() {
            this.hasRunRAF = 1;
        });
        """
    )
    ReplayWrapper.RunActions(action_runner);
    action_runner.WaitForJavaScriptCondition("this.hasRunRAF == 1")

class ReplayPageSet(story.StorySet):
  """A single blank page."""

  def __init__(self):
    super(ReplayPageSet, self).__init__(archive_data_file='data/top10_blank.json',
      cloud_storage_bucket=story.PUBLIC_BUCKET)
    self.AddStory(ReplayPage('file://blank_page/blank_page.html', self))


