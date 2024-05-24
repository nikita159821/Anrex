import requests
import json
import os
import argparse

# Парсинг аргументов командной строки
parser = argparse.ArgumentParser()
parser.add_argument("--github-repository", required=True, help="GitHub repository name in the format 'owner/repo'")
args = parser.parse_args()

# Получение списка ключей шифрования
url = f"https://api.github.com/repos/{args.github_repository}/actions/secrets/public-keys"
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {os.environ["GITHUB_TOKEN"]}',
    'X-GitHub-Api-Version': '2022-11-28'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    keys = json.loads(response.text)['keys']
    for key in keys:
        if key['name'] == 'REPORT_NUMBER_2':
            key_id = key['key_id']
            break
    else:
        print("Ошибка: ключ шифрования для REPORT_NUMBER_2 не найден")
        exit(1)

    # Получение существующего значения секрета
    url = f"https://api.github.com/repos/{args.github_repository}/actions/secrets/REPORT_NUMBER_2"
    response = requests.get(url, headers=headers)
    existing_secret = json.loads(response.text)

    # Расшифровка существующего значения
    from cryptography.fernet import Fernet
    fernet = Fernet(key_id.encode())
    existing_value = fernet.decrypt(existing_secret['encrypted_value'].encode()).decode()

    # Увеличение значения на 1
    new_value = str(int(existing_value) + 1)

    # Зашифровка нового значения
    new_encrypted_value = fernet.encrypt(new_value.encode()).decode()

    # Обновление секрета с новым значением
    payload = {
        "encrypted_value": new_encrypted_value,
        "key_id": key_id
    }
    response = requests.put(url, headers=headers, data=json.dumps(payload))

    print(f"GitHub API response status code: {response.status_code}")
    print(f"GitHub API response text: {response.text}")
    print(f"REPORT_NUMBER_2 value after update: {os.environ['REPORT_NUMBER_2']}")

    if response.status_code == 204:
        print("Секрет успешно обновлен")
    else:
        print(f"Ошибка обновления секрета: {response.status_code} - {response.text}")
else:
    print(f"Ошибка: {response.status_code} - {response.text}")
