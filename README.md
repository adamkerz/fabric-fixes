# fabric-fixes
Fixes for fabric bugs or deficiencies

To use:
import fabric_fixes

Monkey patches fabric's api module to:
 - modify put to take user and group parameters and set them for all files uploaded
 - add a mkdir function that also does chmod/own/grp and optionally with use_sudo
 - add a chmod function that can run chmod/own/grp as required an optionally with sudo (use_sudo)
