import pythoncom
import win32com


def open_doc(sw_app, file_path):
    """Returns opened document"""
    sw_doc = sw_app.OpenDocSilent(
        file_path,
        1,
        win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, -1),
    )
    return sw_doc


if __name__ == '__main__':
    from utils.start_sw import start_sw

    app = start_sw()
    doc = open_doc(app, 'E:\\Files\\KPI\\macro\\Деталь1.SLDPRT')
