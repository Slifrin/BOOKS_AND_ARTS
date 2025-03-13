import paramiko
import re
import stat
import io


def list_files_to_download_v2(items_to_process, client, current_root=".", separator="/"):
    found_elements = []
    for dir_element_attrs in client.listdir_attr(current_root):

        element_full_path = f"{current_root}{separator}{dir_element_attrs.filename}"

        if stat.S_ISDIR(dir_element_attrs.st_mode):
            found_elements.extend(
                list_files_to_download_v2(items_to_process, client, element_full_path)
            )
        else:
            for item in items_to_process:
                if re.search(item, element_full_path):
                    found_elements.append(element_full_path)

    return found_elements


def main() -> None:
    print(f"Hello main from : {__file__}")
    pattern = r".*\.png"

    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect("test.rebex.net", username="demo", password="password")

    client = ssh.open_sftp()

    root = client.stat('.')
    print(root)
    items = list_files_to_download_v2([pattern], client)
    for item in items:
        print(item)
    tmp = io.BytesIO()
    client.getfo(items[-1], tmp)

    print("hello")

if __name__ == "__main__":
    main()
