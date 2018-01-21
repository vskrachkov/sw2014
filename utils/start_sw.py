import win32com.client
import pythoncom

pythoncom.CoInitializeEx(pythoncom.COINIT_MULTITHREADED)


def start_sw(sw_version='2014', visible=1):
    try:
        # last digit in the solid works version
        sw_year_last_digit = int(sw_version[-1])
    except (ValueError, TypeError) as err:
        raise Exception('Invalid SolidWorks version. Origin exception: {} {}'
                        .format(err.__class__.__name__, err))

    # build name of the solid works application
    sw_app_name = 'SldWorks.Application.{}'.format(20 + (sw_year_last_digit - 2))

    # run solid works
    sw_app = win32com.client.DispatchEx(sw_app_name)

    # make started sw app visible or invisible
    sw_app.Visible = visible

    return sw_app


if __name__ == '__main__':
    start_sw(sw_version='2014', visible=1)
