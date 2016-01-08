'''
    ustvnow XBMC Plugin
    Copyright (C) 2015 Lunatixz

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import datetime, time, _strptime, os, urllib
import xbmc, xbmcaddon, xbmcvfs

from resources.lib import Addon

while (not xbmc.abortRequested):
    email = Addon.get_setting('email')
    password = Addon.get_setting('password')
    
    if int(Addon.get_setting('write_type')) != 0 and email != '' and password != '':

        if int(Addon.get_setting('write_type')) in [2,3]:
            MSG = 'M3U'
        else:
            MSG = 'STRM'

        now  = datetime.datetime.today()
        
        try:
            Update_LastRun = Addon.getProperty("Update_NextRun")
            if not Update_LastRun or xbmcvfs.exists(os.path.join(Addon.get_setting('write_folder'),'xmltv.xml')) == False:
                raise exception()
        except:
            Update_LastRun = "1970-01-01 23:59:00.000000"
            Addon.setProperty('Update_NextRun', str(Update_LastRun))
        
        try:
            SyncUpdate = datetime.datetime.strptime(Update_LastRun, "%Y-%m-%d %H:%M:%S.%f")
        except:
            SyncUpdate = datetime.datetime.strptime(Update_LastRun, "%Y-%m-%d %H:%M:%S.%f")

        if now > SyncUpdate:
            xbmc.executebuiltin("XBMC.RunPlugin(plugin://plugin.video.ustvnow/?mode=playlist)")
            
            if Addon.get_setting('silent') == 'false':
                xbmc.executebuiltin("Notification( %s, %s, %d, %s)" % ("USTVnow", "%s/XMLTV Updated" %MSG, 1000, Addon.ICON) )
        
        Update_NextRun = ((now + datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S.%f"))
        Addon.setProperty('Update_NextRun', str(Update_NextRun))
    # Sleep for 1min
    xbmc.sleep(60000)