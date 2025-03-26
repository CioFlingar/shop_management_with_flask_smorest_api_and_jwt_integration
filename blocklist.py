"""
blocklist.py

Ths file just contains the blocklist of the jwt tokens.
 It will be imported by app and the logout resource
 so that tokens can be added to the blocklist when the user logs out.
"""

BLOCKLIST = set()
