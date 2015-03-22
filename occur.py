import sublime
import sublime_plugin
import functools

class OccurCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    filename = self.view.file_name()
    self.view.window().show_input_panel(
      'Pattern:',
      '',
      self.pattern_given,
      None,  # No 'change' handler
      None   # No 'cancel' handler
    )

  # The user has specified a pattern to find occurrences of.
  def pattern_given(self, pattern):
    self.find_results = self.view.find_all(pattern, sublime.IGNORECASE)
    # sublime.
    print(pattern)
    print(self.find_results)
    self.view.window().show_quick_panel(
      # Show entire line comprising the matched occurrence
      [self.view.substr(self.view.line(x)) for x in self.find_results],

      self.occurrence_chosen,      # Callback
      sublime.MONOSPACE_FONT,      # Options
      0,                           # Starting index
      self.occurrence_highlighted  # Callback
    )

  # User highlighted an occurrence
  def occurrence_highlighted(self, i):
    # Center the occurrence, so the user can 'preview' it
    self.view.show_at_center(self.find_results[i])

  # User chose an occurrence to inspect
  def occurrence_chosen(self, i):
    self.view.show_at_center(self.find_results[i])
