"""
    https://python.plainenglish.io/how-to-send-desktop-notifications-with-python-62a738850fbf
    something is't right
"""


from plyer import notification


notification.notify(
    title = 'testing',
    message = 'spr_message',
    app_icon = None,
    timeout = 10
)