class Keyboard:
    KEY_CODES = {
        'LeftMouseButton': 1, 'RightMouseButton': 2, 'ControlBreak': 3,
        'MiddleMouseButton': 4, 'X1MouseButton': 5, 'X2MouseButton': 6,
        'Backspace': 8, 'Tab': 9, 'Clear': 12, 'Enter': 13, 'Pause': 19,
        'CapsLock': 20, 'Escape': 27, 'Space': 32, 'PageUp': 33,
        'PageDown': 34, 'End': 35, 'Home': 36, 'LeftArrow': 37,
        'UpArrow': 38, 'RightArrow': 39, 'DownArrow': 40, 'Select': 41,
        'Print': 42, 'Execute': 43, 'PrintScreen': 44, 'Ins': 45,
        'Delete': 46, 'Help': 47, 'Key0': 48, 'Key1': 49, 'Key2': 50,
        'Key3': 51, 'Key4': 52, 'Key5': 53, 'Key6': 54, 'Key7': 55,
        'Key8': 56, 'Key9': 57, 'A': 65, 'B': 66, 'C': 67, 'D': 68,
        'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74,
        'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80,
        'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86,
        'W': 87, 'X': 88, 'Y': 89, 'Z': 90,
        'LeftWindowsKey': 91, 'RightWindowsKey': 92, 'Application': 93,
        'Sleep': 95, 'NumpadKey0': 96, 'NumpadKey1': 97, 'NumpadKey2': 98,
        'NumpadKey3': 99, 'NumpadKey4': 100, 'NumpadKey5': 101,
        'NumpadKey6': 102, 'NumpadKey7': 103, 'NumpadKey8': 104,
        'NumpadKey9': 105, 'Multiply': 106, 'Add': 107, 'Separator': 108,
        'Subtract': 109, 'Decimal': 110, 'Divide': 111, 'F1': 112,
        'F2': 113, 'F3': 114, 'F4': 115, 'F5': 116, 'F6': 117, 'F7': 118,
        'F8': 119, 'F9': 120, 'F10': 121, 'F11': 122, 'F12': 123,
        'NumLock': 144, 'ScrollLock': 145, 'LeftShift': 160,
        'RightShift': 161, 'LeftControl': 162, 'RightControl': 163,
        'LeftMenu': 164, 'RightMenu': 165, 'BrowserBack': 166,
        'BrowserRefresh': 168, 'BrowserStop': 169, 'BrowserSearch': 170,
        'BrowserFavorites': 171, 'BrowserHome': 172, 'VolumeMute': 173,
        'VolumeDown': 174, 'VolumeUp': 175, 'NextTrack': 176,
        'PreviousTrack': 177, 'StopMedia': 178, 'PlayMedia': 179,
        'StartMailKey': 180, 'SelectMedia': 181, 'StartApplication1': 182,
        'StartApplication2': 183
    }

    @classmethod
    def get_key_code(cls, key_name):
        return cls.KEY_CODES.get(key_name, None)