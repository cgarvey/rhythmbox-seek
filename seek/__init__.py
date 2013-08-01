#
# Rythmbox Plugin to add menu items (and keyboard
# shortcuts) to seek forward (10 secs) / backward (5 secs)
# in the currently playing track.
#
# VERSION 1.0
#

# Copyright 2013 Cathal Garvey. http://cgarvey.ie/
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from gi.repository import GObject, RB, Peas
from gi.repository import Gtk

ui_menu_action = """
<ui>
	<menubar name="MenuBar">
		<menu name="ControlMenu" action="Control">
			<separator />
			<menuitem name="SeekPluginBackward" action="SeekPluginBackward" />
			<menuitem name="SeekPluginForward" action="SeekPluginForward" />
		</menu>
	</menubar>
</ui>
"""

seek_backward_time = 5
seek_forward_time = 10

class TrackSeekPlugin( GObject.Object, Peas.Activatable ):
	object = GObject.property( type=GObject.Object )

	def __init__(self):
		super( TrackSeekPlugin, self ).__init__()

	def do_activate(self):
		print "Activating Plugin\n"

		shell = self.object

		action_group = Gtk.ActionGroup( 'SeekPluginActionGroup' )

		action = Gtk.Action( 'SeekPluginBackward', _('Seek _Backward'), _('Seek backward, in current track, by 5 seconds.'), "" )
		action.connect( 'activate', self.on_skip_backward, shell )
		action_group.add_action_with_accel( action, "<Control>Left" )

		action = Gtk.Action( 'SeekPluginForward', _('Seek _Forward'), _('Seek forward, in current track, by 10 seconds.'), "" )
		action.connect( 'activate', self.on_skip_forward, shell )
		action_group.add_action_with_accel( action, "<Control>Right" )

		shell.props.ui_manager.insert_action_group( action_group )
		shell.props.ui_manager.add_ui_from_string (ui_menu_action)
		
	def on_skip_backward( self, *args ):
		print "Seeking backward\n"
		sp = self.object.props.shell_player

		if( sp.get_playing()[1] ):
			seek_time = sp.get_playing_time()[1] - seek_backward_time
			if( seek_time < 0 ): seek_time = 0

			print "Seeking backward to %d sec(s)\n" % seek_time
			sp.set_playing_time( seek_time )
			print "Done.\n";
		else: print "Not playing, refusing to seek backward\n"

	def on_skip_forward( self, *args ):
		print "Seeking forward\n"
		sp = self.object.props.shell_player

		if( sp.get_playing()[1] ):
			seek_time = sp.get_playing_time()[1] + seek_forward_time
			song_duration = sp.get_playing_song_duration()
			if( song_duration > 0 ): #sanity check
				if( seek_time > song_duration ): seek_time = song_duration
			
				print "Seeking forward to %d sec(s)\n" % seek_time
				sp.set_playing_time( seek_time )
				print "Done.\n";
			else: print "Song duration is reported as 0. Refusing to seek!\n"
		else: print "Not playing, refusing to seek forward\n"
		
	def do_deactivate(self):
		print "De-activating Plugin\n"

