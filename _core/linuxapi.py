

import subprocess
from string import Template

notify_send_template = Template(
    "notify-send \"${title}\" \"${message}\" --icon=${icon_path} --expire-time=${expiration}"
)

notify_send_without_icon_template = Template(
    "notify-send \"${title}\" \"${message}\""
)



# notify-send '202020Rule' 'ITS TIME NOW !!!' --icon=/home/alexzander/Alexzander__/programming/python/202020_order/assets/icons/202020-order-icon.png


def linux_notification(title, message, icon_path=None, exp=10):
    if icon_path:
        command = notify_send_template.safe_substitute(
            title=title,
            message=message,
            icon_path=icon_path,
            expiration=exp * 1000
        )
        # print(command)
        subprocess.call(command, shell=True)
    else:
        subprocess.call(notify_send_without_icon_template.safe_substitute(
            title=title,
            message=message,
        ), shell=True)



if __name__ == '__main__':
    linux_notification(
        "title from code",
        "message from code",
        "/home/alexzander/Alexzander__/programming/python/202020_order/assets/icons/202020-order-icon.png"
    )
