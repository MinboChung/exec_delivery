import win32api
import win32con
import win32file
import win32gui

def set_publisher_info(file_path, publisher_name):
    # Open the file for writing
    hfile = win32file.CreateFile(
        file_path,
        win32file.GENERIC_WRITE,
        win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE,
        None,
        win32con.OPEN_EXISTING,
        0,
        None
    )

    # Get existing file version info
    version_info = win32api.GetFileVersionInfo(file_path, "\\")

    # Update the publisher information
    version_info['StringFileInfo'] = {
        win32con.LANG_NEUTRAL: {
            win32con.BLOCK_UNTITLED: f'Publisher\0{publisher_name}\0\0\0\0\0\0\0\0\0'
        }
    }

    # Set the updated version info
    win32api.SetFileAttributes(file_path, win32con.FILE_ATTRIBUTE_NORMAL)
    win32api.SetFileVersionInfo(
        file_path,
        '\\',
        version_info
    )
    win32file.CloseHandle(hfile)

# Replace 'your_executable_path.exe' and 'Your Publisher Name' with your file path and desired publisher name
set_publisher_info('./dist/testing.exe', 'Minbo Chung')
