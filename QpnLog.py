from enum import Enum
from QpnSettings import QpnSettings

class MessageType(Enum):
    Debug = 1
    Warning = 2
    Error = 3
    General = 4

def LogMessage(messageType: MessageType, messageText: str, messageLocation: str = None):
    if messageType == MessageType.Debug and not QpnSettings.DEBUG:
        # ignore message, as debug is disabled
        return

    if messageLocation is None:
        print('{}: {}'.format(MessageType(messageType).name), messageText)
    else:
        print('{} - {}: {}'.format(messageType.name, messageLocation, messageText))
